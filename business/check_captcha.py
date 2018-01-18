#校验验证码
from business.damatuWeb import DamatuApi
from business.captcha_download import download_captcha
import json
from business.urlcontants import UrlContants
from business.middleproxy import MiddleProxy

#坐标识别式验证码
CAPTCHA_TYPE = 310
#坐标偏移量
OFFSET_X = 0
OFFSET_Y = 30

def get_result_points(ret,result):
    result_point = ''
    if ret == 0:
        if result is not None:
            captcha_point = result.split('|')
            for point in captcha_point:
                if point is not None:
                    pointX = point.split(',')[0]
                    pointY = point.split(',')[1]
                    pointX = int(pointX) - OFFSET_X
                    pointY = int(pointY) - OFFSET_Y
                    result_point = result_point + str(pointX) + ',' + str(pointY)+','
        return result_point.rstrip(',')
    else:
        print('打码故障！ 错误代码：%s' % ret)
        return None

def check_captcha_request(url,param):

    params={'answer':param,
            'login_site':'E',
            'rand':'sjrand'}
    s = MiddleProxy.getSession().post(url, params=params,headers=MiddleProxy.headers_xhr)
    if s.status_code == 200 and s.content is not None:
        content = str(s.content,encoding='utf-8')
        jres = json.loads(content)
        print(jres)
        return jres

def check_captcha():
    #存储验证码图片
    image_path = download_captcha()
    if image_path is not None:
        damatu = DamatuApi(MiddleProxy.getDm2User(),MiddleProxy.getDm2Pwd())
        #使用打码兔获取验证码
        print(damatu.getBalance())
        ret,result,id = damatu.decode(image_path,310)
        print('打码兔提供--->'+result)
        #获取转换后的坐标
        result_points = get_result_points(ret,result)
        print('打码兔坐标转换--->'+result_points)
        #发起验证码验证
        check_result = check_captcha_request(UrlContants.CAPTCHA_CHECK,result_points)
        if check_result['result_code'] == '4':
            #此处后续可以进行数据库存储，因12306验证码图片不是动态生成的，可以存储对应的答案，减少对打码平台的依赖
            return True
        else:
            return False
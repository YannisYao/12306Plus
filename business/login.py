#12306账号登陆类
import requests
from business.check_captcha import check_captcha
import json
from bs4 import BeautifulSoup
from business.urlcontants import UrlContants
from business.middleproxy import MiddleProxy

def check_login(url=UrlContants.LOGIN_URL):

    params = {'username': MiddleProxy.get12306User(),
              'password': MiddleProxy.get12306Pwd(),
              'appid': 'otn'}
    s = MiddleProxy.getSession().post(url,params=params,headers=MiddleProxy.headers_xhr)
    if s.status_code == 200 and s.content is not None:
        content = str(s.content,encoding='utf-8')
        jres = json.loads(content)
        print(jres)
        return jres

def uamtk_request():
    uamtk_params = {
        'appid':'otn'
    }
    s = MiddleProxy.getSession().post(UrlContants.UAMTK_REQUEST,headers=MiddleProxy.headers_xhr,params=uamtk_params)
    if s.status_code == 200 :
        content = str(s.content,encoding='utf-8')
        jres1 = json.loads(content)
        print(jres1)
        if jres1['result_code'] == 0 :
            newapptk = jres1['newapptk']
            uamtk_auth_params = {
                "tk":newapptk
            }
            ss = MiddleProxy.getSession().post(UrlContants.UAMTK_AUTH_CLIENT,headers=MiddleProxy.headers_xhr,params=uamtk_auth_params)
            if ss.status_code == 200:
                jres2 = json.loads(str(ss.content,encoding='utf-8'))
                print(jres2)
                if jres2['result_code'] == 0:
                    print('验证通过！')
                    return True #后续可以从首页开始爬虫
    return False

def query_userinfo(url=UrlContants.QUERY_USERINFO):
    params = {'_json_att':''}
    s = MiddleProxy.getSession().post(url,headers=MiddleProxy.headers_doc,params=params)
    if s.status_code == 200 :
        html = str(s.content,encoding='utf-8')
        bsObj = BeautifulSoup(html,'html.parser')
        item_infos = bsObj.findAll('div',{'class':'info-item'})
        for item in item_infos:
            print(item.get_text())





def login():
    if check_captcha() :
        login_result = check_login()
        if login_result is not None and login_result['result_code'] == 0:
            print('登陆成功！')
            #uamtk = login_result['uamtk']
            if uamtk_request():
                print('校验成功！')
                #此处以后就可以做一些刷票订票的操作了
                query_userinfo()
                return True

    print('登陆失败！')
    print('准备重新登录！')
    MiddleProxy.clearSession()
    login()
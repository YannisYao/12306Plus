#存放各种url
class UrlContants(object):
    # 首先获取图片，然后给图片进行md5摘要取名
    CAPTCHA_URL = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.5537893176239919'
    # 验证码校验接口
    CAPTCHA_CHECK = 'https://kyfw.12306.cn/passport/business/business-check'

    # 12306 登陆接口
    LOGIN_URL = 'https://kyfw.12306.cn/passport/web/login'
    #uamtk 校验接口
    UAMTK_REQUEST = 'https://kyfw.12306.cn/passport/web/auth/uamtk'
    UAMTK_AUTH_CLIENT = 'https://kyfw.12306.cn/otn/uamauthclient'
    #个人中心首页页面
    MY_FIRST_PAGE = 'https://kyfw.12306.cn/otn/login/userLogin'
    MY_FIRST_PAGE_REDIRECT = 'https://kyfw.12306.cn/otn/index/initMy12306'
    #用户信息查询接口
    QUERY_USERINFO = 'https://kyfw.12306.cn/otn/modifyUser/initQueryUserInfo'
    #余票预查询接口
    PRE_STANDBY_TICKET = 'https://kyfw.12306.cn/otn/leftTicket/log'
    #余票查询接口
    STANDBY_TICKET = 'https://kyfw.12306.cn/otn/leftTicket/queryA'
    #校验用户接口
    CHECK_USER = 'https://kyfw.12306.cn/otn/login/checkUser'


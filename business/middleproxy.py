#中间件代理类
import requests
from fake_useragent import UserAgent
class MiddleProxy(object):
    _session = None
    _ua = UserAgent(verify_ssl=False)
    _12306_user = ''
    _12306_pwd = ''
    _dm2_user = ''
    _dm2_passwd = ''

    headers_image = {'Host': 'kyfw.12306.cn', 'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Accept-Encoding': 'gzip, deflate, br',
               'User-Agent': _ua.random}
    headers_xhr = {'Host': 'kyfw.12306.cn', 'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
               'Accept-Encoding': 'gzip, deflate, br',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Referer':'https://kyfw.12306.cn/otn/login/init',
               'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': _ua.random}
    headers_doc = {'Host': 'kyfw.12306.cn', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Accept-Encoding': 'gzip,deflate,br',
               'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
               'User-Agent': _ua.random}

    #单例session，方便管理
    @classmethod
    def getSession(cls):
        if MiddleProxy._session is None:
            MiddleProxy._session = requests.session()
            #MiddleProxy._session.verify = False
        return MiddleProxy._session

    @classmethod
    def clearSession(cls):
        if MiddleProxy._session is not None:
            MiddleProxy._session = None

    @classmethod
    def set12306User(cls,user):
        MiddleProxy._12306_user = user

    @classmethod
    def get12306User(cls):
        return MiddleProxy._12306_user

    @classmethod
    def set12306Pwd(cls, pwd):
        MiddleProxy._12306_pwd = pwd

    @classmethod
    def get12306Pwd(cls):
        return MiddleProxy._12306_pwd

    @classmethod
    def setDm2User(cls, user):
        MiddleProxy._dm2_user = user

    @classmethod
    def getDm2User(cls):
        return MiddleProxy._dm2_user

    @classmethod
    def setDm2Pwd(cls, pwd):
        MiddleProxy._dm2_passwd = pwd

    @classmethod
    def getDm2Pwd(cls):
        return MiddleProxy._dm2_passwd



# if __name__ == '__main__':
#     a = MiddleProxy.getSession()
#     b = MiddleProxy.getSession()
#     c = MiddleProxy.getSession()
#     print(id(a),id(b),id(c))
#     MiddleProxy.clearSession()
#     d = MiddleProxy.getSession()
#     print(id(d))
#调度函数
#去除警告
# from urllib3 import disable_warnings
# from urllib3.exceptions import InsecureRequestWarning
# disable_warnings(InsecureRequestWarning)
from business.login import login
from business.middleproxy import MiddleProxy
import sys

def exitSys(code):
    if code == 'Q':
        sys.exit()

def inputMsg():
    print('**==============================**'+"输入Q可退出本系统")
    _12306_user = input('请输入12306用户名：')
    exitSys(_12306_user)
    MiddleProxy.set12306User(_12306_user)
    _12306_pwd = input('请输入12306密码：')
    exitSys(_12306_pwd)
    MiddleProxy.set12306Pwd(_12306_pwd)
    dm2_user = input('请输入打码兔用户名：')
    exitSys(dm2_user)
    MiddleProxy.setDm2User(dm2_user)
    dm2_pwd = input('请输入打码兔密码：')
    exitSys(dm2_pwd)
    MiddleProxy.setDm2Pwd(dm2_pwd)

if __name__ == '__main__':
    inputMsg()
    login()

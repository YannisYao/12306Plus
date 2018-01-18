# -*- coding:utf-8 -*-

'''
登陆界面
author: yannis
website: www.yanniszone.com
'''

from PyQt5.QtWidgets import QMainWindow,QMessageBox
from business.loadcaptachthread import LoadCaptchaThread
from uicontrollers.u_captcha_dialog import Ui_captcha
from uicontrollers.captcha_dialog import CaptchaDialog
import re
from business.middleproxy import MiddleProxy
from business.checkcaptchathread import CheckCaptchaThread


class LoginWidget(QMainWindow):

    def __init__(self,mainWindow):
        super(LoginWidget, self).__init__()
        self.captchaDialog = CaptchaDialog(self)
        self.captchaDialog.dialogSucess.connect(self.inputPointSucess)
        self.uiCaptcha = Ui_captcha()
        self.uiCaptcha.setupUi(self.captchaDialog)
        self.mainWindow = mainWindow
        self.mainWindow.setupUi(self)
        self.loginState = False
    #button 点击监听
    def buttonClicked(self):
        sender = self.sender()
        print(sender.objectName())
        if sender.objectName() == 'loginButton' and not self.captchaDialog.isVisible():
            flag,msg = self.checkUserAndPwd()
            if flag:
                # 切换到登陆状态
                self.mainWindow.changeLoginingState(1)
                self.loginState = True
                self.requestCaptcha()
            else:
                QMessageBox.about(self, '提示信息', '\n'+msg)
        elif sender.objectName() == 'signup':
            #调用浏览器跳转12306注册页面
            pass
        elif sender.objectName() == 'cancelbutton':
            self.exitLogin()

    #校验用户名密码
    def checkUserAndPwd(self):
        match1 = r'^(13[0-9])|(14[0-9])|(15[0-9])|(18[0-9])|(17[0-9])|(16[0-9])|(19[0-9])\d{8}$'
        match2 = r'^[A-Za-z]{1}([A-Za-z0-9]|[_]){0,29}$'
        match3 = r"^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])" \
                 r"+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|" \
                 r"((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|" \
                 r"\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|" \
                 r"(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*" \
                 r"(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d" \
                 r"|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|" \
                 r"(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]" \
                 r"|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|" \
                 r"\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|" \
                 r"[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|" \
                 r"(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|"\
                 r"\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|" \
                 r"[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))$"
        username = self.mainWindow.userEdit.text()
        pwd = self.mainWindow.userEdit_2.text()
        if not re.match(match1,username) and not re.match(match2,username) and not re.match(match3,username):
            return (False,'用户名格式错误！')
        if pwd is None or pwd == '' or len(pwd)< 6 :
            return (False,'密码不能为空，且至少为6位')
        self.saveUserAndPwd(username,pwd)
        return (True,None)


    def saveUserAndPwd(self,username,pwd):
        MiddleProxy.set12306User(username)
        MiddleProxy.set12306Pwd(pwd)

    def requestCaptcha(self):
        loadCaptchaThread = LoadCaptchaThread(self)
        loadCaptchaThread.sinOut.connect(self.captchaDialog.displayCaptcha)
        loadCaptchaThread.sinFalure.connect(self.failCaptcha)
        loadCaptchaThread.start()

    def failCaptcha(self,strs):
        reply = QMessageBox.question(self,'提示信息',strs+"\n是否重新请求验证码？",
                             QMessageBox.Yes |QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.requestCaptcha()
        else:
            self.exitLogin()

    def exitLogin(self):
        if self.captchaDialog.isVisible():
            self.captchaDialog.reject()
        else:
            self.mainWindow.changeLoginingState(0)
            self.loginState = False

    def dialogAccepted(self):
        pass

    def dialogRejected(self):
        self.mainWindow.changeLoginingState(0)
        self.loginState = False

    def inputPointSucess(self,absPoint):
        """
        :param absPoint: 验证码Dialog回传的坐标
        :return:
        """
        self.checkLogin(absPoint)

    def checkLogin(self,absPoint):
        checkCaptchaThread = CheckCaptchaThread(self, absPoint)
        checkCaptchaThread.captchaFalure.connect(self.checkCaptchaFail)
        checkCaptchaThread.loginFalure.connect(self.loginFail)
        checkCaptchaThread.loginSucess.connect(self.loginSucess)
        checkCaptchaThread.start()


    def checkCaptchaFail(self,msg):
        QMessageBox.about(self, '提示信息', '\n' + msg)

    def loginFail(self,msg):
        QMessageBox.about(self, '提示信息', '\n' + msg)

    def loginSucess(self,msg):
        QMessageBox.about(self, '提示信息', '\n' + msg)

    #check监听
    def checkChanged(self,state):
        print(state)


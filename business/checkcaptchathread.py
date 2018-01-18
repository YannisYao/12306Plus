from PyQt5.QtCore import QThread,pyqtSignal
from business.check_captcha import check_captcha_request
from business.login import check_login,uamtk_request


class CheckCaptchaThread(QThread):
    loginFalure  = pyqtSignal(str)
    captchaFalure = pyqtSignal(str)
    loginSucess = pyqtSignal(str)

    def __init__(self,parent=None,result_points=None):
        super(CheckCaptchaThread, self).__init__(parent)
        self.result_points =result_points

    def run(self):
        check_result = check_captcha_request(self.result_points)
        if check_result['result_code'] == '4':
            login_result = check_login()
            if login_result['result_code'] == 0:
                uamtk_request()
                self.loginSucess.emit("登陆成功！")
            else:
                self.loginFalure.emit("登陆失败！")

        else:
            self.captchaFalure.emit("校验验证码失败！")






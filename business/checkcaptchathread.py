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
        check_result,msg = check_captcha_request(self.result_points)
        if check_result:
            login_result,msg1,flag= check_login()
            if login_result:
                username = None
                while(username is None):
                    username = uamtk_request()

                self.loginSucess.emit(username)
            else:
                self.loginFalure.emit(str(flag)+"|"+msg1)

        else:
            self.captchaFalure.emit(msg)






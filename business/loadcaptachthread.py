from PyQt5.QtCore import QThread,pyqtSignal
from business.captcha_download import download_captcha


class LoadCaptchaThread(QThread):
    sinOut  = pyqtSignal(bytes)
    sinFalure = pyqtSignal(str)

    def __init__(self,parent=None):
        super(LoadCaptchaThread, self).__init__(parent)

    def run(self):
        flag,content = download_captcha()
        if flag:
            self.sinOut.emit(content)
        else:
            self.sinFalure.emit(content)






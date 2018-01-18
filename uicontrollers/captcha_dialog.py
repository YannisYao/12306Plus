# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QDialog,QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal

class CaptchaDialog(QDialog):
    dialogSucess = pyqtSignal(str)

    def __init__(self,parent=None):
        super(CaptchaDialog, self).__init__(parent)
        self.requestCaptchaing = False
        if parent is not None:
            self.accepted.connect(parent.dialogAccepted)
            self.rejected.connect(parent.dialogRejected)

    def displayCaptcha(self,image):
        uiCatcha = self.parent().uiCaptcha
        pix = QPixmap()
        pix.loadFromData(image)
        uiCatcha.label.setPixmap(pix)
        self.show()
        # uiCatcha.label.show()
        # uiCatcha.refresh.show()
        self.refreshingState(0)

    def refreshCaptcha(self):
        if not self.requestCaptchaing:
            self.refreshingState(1)
            self.parent().requestCaptcha()

    def refreshingState(self,state):
        uiCatcha = self.parent().uiCaptcha
        if state == 1:#刷新ing
            uiCatcha.label.hide()
            uiCatcha.refresh.hide()
            uiCatcha.captchaProgressBar.show()
            self.requestCaptchaing = True
        else:
            uiCatcha.label.show()
            uiCatcha.refresh.show()
            uiCatcha.captchaProgressBar.hide()
            self.requestCaptchaing = False

    def acceptOk(self):
        uiCatcha = self.parent().uiCaptcha
        abspoint = uiCatcha.label.getPointXAndYs()
        if abspoint is not None:
            self.accept()
            self.dialogSucess.emit(abspoint)
        else:
            QMessageBox.about(self, '提示信息', '\n请点击验证码！')


    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示',
                                     "您确定要退出退出登录么?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.reject()
        else:
            event.ignore()







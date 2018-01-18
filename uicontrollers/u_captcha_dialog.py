# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from uicontrollers.circlepointprogressbar import CirlcePointProgressBar
from uicontrollers.diyqlabel import PaintQLabel
import uicontrollers.resources

class Ui_captcha(object):
    def setupUi(self, captcha):
        captcha.setObjectName("business")
        captcha.resize(400, 300)
        captcha.setMinimumSize(QtCore.QSize(400, 300))
        captcha.setMaximumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        captcha.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(captcha)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setText("确定")
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).setText("取消")
        self.label = PaintQLabel(captcha)
        self.label.setGeometry(QtCore.QRect(40, 20, 293, 190))
        self.label.setText("")
        self.label.setObjectName("label_captach")
        self.label.hide()
        self.refresh = QtWidgets.QPushButton(captcha)
        self.refresh.setGeometry(QtCore.QRect(300, 20, 25, 25))
        self.refresh.setText("")
        self.refresh.setObjectName("refresh")
        #self.refresh.setStyleSheet("border:none");
        self.refresh.setFlat(True);
        self.refresh.setIcon(QtGui.QIcon(':/images/refresh.png'))
        self.refresh.setIconSize(QtCore.QSize(25,25))
        self.refresh.clicked.connect(captcha.refreshCaptcha)
        self.refresh.hide()

        # 加入进度条，影藏
        self.captchaProgressBar = CirlcePointProgressBar(captcha)
        self.captchaProgressBar.setGeometry(QtCore.QRect(170, 120, 60, 60))
        self.captchaProgressBar.setObjectName("d_progressbar")
        self.captchaProgressBar.hide()

        self.retranslateUi(captcha)
        self.setStyleSheet(captcha)
        self.buttonBox.accepted.connect(captcha.acceptOk)
        self.buttonBox.rejected.connect(captcha.reject)
        QtCore.QMetaObject.connectSlotsByName(captcha)

    def retranslateUi(self, captcha):
        _translate = QtCore.QCoreApplication.translate
        captcha.setWindowTitle(_translate("business", "Captcha"))

    def setStyleSheet(self,captcha):
        file = QtCore.QFile(':qss/captchadialog.qss')
        file.open(QtCore.QFile.ReadOnly)
        stylesheet = str(file.readAll(), encoding='utf-8')
        captcha.setStyleSheet(stylesheet)



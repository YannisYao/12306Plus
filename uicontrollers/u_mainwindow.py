# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from uicontrollers.circlepointprogressbar import CirlcePointProgressBar
import uicontrollers.resources

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(400, 300)
        LoginWindow.setMinimumSize(QtCore.QSize(400, 300))
        LoginWindow.setMaximumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(LoginWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(140, 30, 118, 84))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/login.png"))
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox.setGeometry(QtCore.QRect(70, 220, 91, 16))
        self.checkBox.setCheckable(True)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(LoginWindow.checkChanged)
        self.splitter = QtWidgets.QSplitter(self.centralWidget)
        self.splitter.setGeometry(QtCore.QRect(70, 250, 271, 31))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.loginButton = QtWidgets.QPushButton(self.splitter)
        self.loginButton.setObjectName("loginButton")
        self.loginButton.clicked.connect(LoginWindow.buttonClicked)
        self.signup = QtWidgets.QPushButton(self.splitter)
        self.signup.setObjectName("signup")
        self.signup.clicked.connect(LoginWindow.buttonClicked)
        self.splitter_2 = QtWidgets.QSplitter(self.centralWidget)
        self.splitter_2.setGeometry(QtCore.QRect(70, 130, 271, 81))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.userEdit = QtWidgets.QLineEdit(self.splitter_2)
        self.userEdit.setObjectName("userEdit")
        self.userEdit_2 = QtWidgets.QLineEdit(self.splitter_2)
        self.userEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.userEdit_2.setObjectName("userEdit_2")
        #加入进度条，影藏
        self.loginProgressBar = CirlcePointProgressBar(self.centralWidget)
        self.loginProgressBar.setGeometry(QtCore.QRect(170, 145, 60, 60))
        self.loginProgressBar.setObjectName("progressbar")
        self.loginProgressBar.hide()
        #登陆取消按钮
        self.cancleButton = QtWidgets.QPushButton(self.centralWidget)
        self.cancleButton.setObjectName('cancelbutton')
        self.cancleButton.setGeometry(QtCore.QRect(130, 230, 140, 31))
        self.cancleButton.clicked.connect(LoginWindow.buttonClicked)
        self.cancleButton.hide()

        LoginWindow.setCentralWidget(self.centralWidget)

        self.setStyleSheet(LoginWindow)
        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.checkBox.setText(_translate("LoginWindow", "记住密码"))
        self.loginButton.setText(_translate("LoginWindow", "登陆"))
        self.signup.setText(_translate("LoginWindow", "注册"))
        self.cancleButton.setText(_translate("LoginWindow", "取消"))
        self.userEdit.setPlaceholderText(_translate("LoginWindow", "请输入12306用户名"))
        self.userEdit_2.setPlaceholderText(_translate("LoginWindow", "请输入12306密码"))

    def setStyleSheet(self,LoginWindow):
        file = QtCore.QFile(':/qss/loginwindow.qss')
        file.open(QtCore.QFile.ReadOnly)
        stylesheet = str(file.readAll(),encoding='utf-8')
        LoginWindow.setStyleSheet(stylesheet)

    def changeLoginingState(self,flag):
        if flag == 0:#常态
            self.checkBox.show()
            self.userEdit.show()
            self.userEdit_2.show()
            self.loginButton.show()
            self.signup.show()

            self.cancleButton.hide()
            self.loginProgressBar.hide()
        else:#登陆态
            self.checkBox.hide()
            self.userEdit.hide()
            self.userEdit_2.hide()
            self.loginButton.hide()
            self.signup.hide()

            self.loginProgressBar.show()
            self.cancleButton.show()








from uicontrollers.u_mainwindow import Ui_LoginWindow
from PyQt5.QtWidgets import QApplication
from uicontrollers.login_widget import LoginWidget
import sys

if __name__ == '__main__':
    app =QApplication(sys.argv)
    mainWidget = LoginWidget(Ui_LoginWindow())
    mainWidget.show()
    sys.exit(app.exec_())


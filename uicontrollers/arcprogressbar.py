# -*- coding:utf-8 -*-

'''
author yannis
自定义旋转progressbar
'''

from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QColor,QPainter,QPen
from PyQt5.QtCore import QTimer,QPointF,QRectF,QSize
from PyQt5.Qt  import Qt
import sys


class CirlceProgressBar(QWidget):
    CICLE_START_COLOR = QColor(1,1,255)
    CICLE_END_COLOR = QColor(128,128,127)
    SPEED = 100

    CIRCLE_WIDTH =8
    #间隔度数
    CIRCLE_SPACE = 5
    #分成多少份
    ARC_NUMS = 8

    def __init__(self,parent=None):
        super(CirlceProgressBar, self).__init__()
        self.updateTimer = QTimer()
        self.updateTimer.setInterval(self.SPEED)
        self.updateTimer.timeout.connect(self.updateAngle)
        self.updateTimer.start()
        self.highlightindex = 0
        #设置为无窗体
        self.setWindowFlags(Qt.FramelessWindowHint)
        #设置背景透明
        self.setAttribute(Qt.WA_TranslucentBackground)
        #外圆的半径
        self.outerRadius = 0


    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        #设置抗锯齿
        painter.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing)
        #画大弧度
        self.drawBigCircle(painter)


    def drawBigCircle(self,painter):
        painter.save()

        self.outerRadius = self.height()/2 -4-self.CIRCLE_WIDTH/2 if self.width() > self.height() else self.width()/2 -4-self.CIRCLE_WIDTH/2

        painter.translate(self.rect().center().x(),self.rect().center().y())

        topLeft = QPointF(-self.outerRadius,-self.outerRadius)
        bottomRight = QPointF(self.outerRadius, self.outerRadius)
        tRect = QRectF(topLeft,bottomRight)

        pen1 = QPen()
        pen1.setWidth(self.CIRCLE_WIDTH)
        pen1.setColor(self.CICLE_END_COLOR)
        pen1.setCapStyle(Qt.FlatCap)
        #pen.setJoinStyle(Qt.RoundJoin)
        painter.setPen(pen1)
        #painter.setPen(Qt.NoPen)
        #painter.setBrush(conGradient)
        painter.setBrush(Qt.NoBrush)
        #painter.drawEllipse(tRect)
        arcwidth = (360-self.ARC_NUMS*self.CIRCLE_SPACE)/self.ARC_NUMS
        for i in range(self.ARC_NUMS):
            if i == self.highlightindex:
                pen1.setColor(self.CICLE_START_COLOR)
                painter.setPen(pen1)
            else:
                pen1.setColor(self.CICLE_END_COLOR)
                painter.setPen(pen1)
            painter.drawArc(tRect, i*self.CIRCLE_SPACE*16+i*arcwidth*16, arcwidth*16)

        painter.restore()


    def sizeHint(self):
        return QSize(50,50)





    def updateAngle(self):
        self.highlightindex += 1
        if self.highlightindex > self.ARC_NUMS-1:
            self.highlightindex = 0

        self.update()
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mybmw = CirlceProgressBar()
    mybmw.show()
    sys.exit(app.exec_())
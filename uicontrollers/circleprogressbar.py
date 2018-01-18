# -*- coding:utf-8 -*-

'''
author yannis
自定义旋转progressbar
'''

from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QColor,QPainter,QConicalGradient,QPen
from PyQt5.QtCore import QTimer,QPointF,QRectF,QSize
from PyQt5.Qt  import Qt
import sys


class CirlceProgressBar(QWidget):
    CICLE_START_COLOR = QColor(1,1,255)
    CICLE_END_COLOR = QColor(255,255,255)

    #CIRCLE_COLOR_LIST = [QColor(1,1,255),QColor(48,47,254),QColor(115,115,253),QColor(171,171,254),QColor(236,236,254),QColor(255,255,255)]

    SPEED = 2
    #圆环的宽度
    CIRCLE_WIDTH = 10

    def __init__(self,parent=None):
        super(CirlceProgressBar, self).__init__()
        self.updateTimer = QTimer()
        self.updateTimer.setInterval(self.SPEED)
        self.updateTimer.timeout.connect(self.updateAngle)
        self.updateTimer.start()
        #旋转角度
        self.angle = 0
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
        painter.rotate(self.angle)

        topLeft = QPointF(-self.outerRadius,-self.outerRadius)
        bottomRight = QPointF(self.outerRadius, self.outerRadius)
        tRect = QRectF(topLeft,bottomRight)
        conGradient = QConicalGradient(0,0,340)
        conGradient.setColorAt(1.0,self.CICLE_START_COLOR)
        conGradient.setColorAt(0.0,self.CICLE_END_COLOR)
        # for i in range(len(self.CIRCLE_COLOR_LIST)):
        #     conGradient.setColorAt((i+1)/len(self.CIRCLE_COLOR_LIST),self.CIRCLE_COLOR_LIST[i])
        pen1 = QPen()
        pen1.setWidth(self.CIRCLE_WIDTH)
        pen1.setBrush(conGradient)
        pen1.setCapStyle(Qt.RoundCap)
        #pen.setJoinStyle(Qt.RoundJoin)
        painter.setPen(pen1)
        #painter.setPen(Qt.NoPen)
        #painter.setBrush(conGradient)
        painter.setBrush(Qt.NoBrush)
        #painter.drawEllipse(tRect)
        painter.drawArc(tRect,0,325*16)
        painter.restore()

    def sizeHint(self):
        return QSize(60,60)





    def updateAngle(self):
        self.angle += 1
        if self.angle > 360:
            self.angle = 0

        self.update()
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mybmw = CirlceProgressBar()
    mybmw.show()
    sys.exit(app.exec_())
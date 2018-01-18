# -*- coding:utf-8 -*-

'''
author yannis
自定义旋转progressbar
'''

from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QColor,QPainter,QBrush,QRadialGradient
from PyQt5.QtCore import QTimer,QPointF,QRectF,QSize
from PyQt5.Qt  import Qt
import sys
import math


class CirlcePointProgressBar(QWidget):
    CIRCLE_POINT_COLOR_LIST = [QColor(38,38,37),QColor(55,55,55),QColor(83,83,82),
                               QColor(118,118,118),QColor(149,149,148),QColor(182,181,182),
                               QColor(207,207,207),QColor(230,230,230)]
    SPEED = 150

    POINT_RADIUS = 5
    #间隔度数
    POINT_NUMS = len(CIRCLE_POINT_COLOR_LIST)


    def __init__(self,parent=None):
        super(CirlcePointProgressBar, self).__init__(parent)
        self.updateTimer = QTimer()
        self.updateTimer.setInterval(self.SPEED)
        self.updateTimer.timeout.connect(self.updateAngle)
        self.updateTimer.start()
        self.highlightindex = 0
        #设置为无窗体
        self.setWindowFlags(Qt.FramelessWindowHint)
        #设置背景透明
        self.setAttribute(Qt.WA_TranslucentBackground)


    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        #设置抗锯齿
        painter.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing)
        #画大弧度
        self.drawBigCircle(painter)

    #通过圆心坐标获取小圆矩阵
    def xPointRectF(self,x,y):
        topLeft = QPointF(x-self.POINT_RADIUS,y-self.POINT_RADIUS)
        bottomRight = QPointF(x+self.POINT_RADIUS,y+self.POINT_RADIUS)
        return QRectF(topLeft,bottomRight)


    def drawBigCircle(self,painter):
        painter.save()
        # 外圆的半径
        outerRadius = self.height()/2 -4-self.POINT_RADIUS if self.width() > self.height() else self.width()/2 -4-self.POINT_RADIUS

        # 二分之根号二
        constant = math.sqrt(2) / 2

        painter.translate(self.rect().center().x(),self.rect().center().y())
        #此坐标是按照逆时针方向
        pointRects = [self.xPointRectF(outerRadius,0),self.xPointRectF(constant * outerRadius,-constant * outerRadius),
                      self.xPointRectF(0,-outerRadius),self.xPointRectF(-constant * outerRadius,-constant * outerRadius),
                      self.xPointRectF(-outerRadius,0),self.xPointRectF(-constant * outerRadius,constant * outerRadius),
                      self.xPointRectF(0,outerRadius),self.xPointRectF(constant * outerRadius,constant * outerRadius)]

        painter.setPen(Qt.NoPen)
        for i in range(self.POINT_NUMS):
            pieGradient = QRadialGradient(pointRects[i].center(), self.POINT_RADIUS, pointRects[i].center())
            pieGradient.setColorAt(0.0, self.CIRCLE_POINT_COLOR_LIST[(i+self.highlightindex) % (self.POINT_NUMS)])
            pieGradient.setColorAt(1.0, self.CIRCLE_POINT_COLOR_LIST[(i+self.highlightindex) % (self.POINT_NUMS)])
            painter.setBrush(pieGradient)
            painter.drawEllipse(pointRects[i])
        painter.restore()


    def sizeHint(self):
        return QSize(60,60)

    def updateAngle(self):
        self.highlightindex += 1
        if self.highlightindex > self.POINT_NUMS-1:
            self.highlightindex = 0

        self.update()
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    progressbar = CirlcePointProgressBar()
    progressbar.show()
    sys.exit(app.exec_())
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtCore import QTimer,QPointF,QRectF,QSize
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter,QColor,QRadialGradient,QTransform
import sys


#自定义宝马标志旋转图标
class MyBMWWidget(QWidget):
    # 内部圆半径比例因子
    RADIUS_FACTOR = 0.8

    #旋转速度 mm
    SPEED = 10

    #外部圆开始和停止颜色
    OUTER_CIRCLE_START_COLOR =  QColor(65,65,65)
    OUTER_CIRCLE_END_COLOR  = QColor(89,89,89)

    #内部圆的蓝色
    BLUE_CIRCLE_START_COLOR  = QColor(0,133,203)
    BLUE_CIRCLE_END_COLOR  = QColor(0,118,177)
    #内部圆的白色
    WHITE_CIRCLE_START_COLOR =  QColor(255,255,255)
    WHITE_CIRCLE_END_COLOR  = QColor(233,233,233)

    def __init__(self,parent=None):
        super(MyBMWWidget, self).__init__()
        self.m_updateTimer = QTimer(self)
        #定时器执行间隔,ms
        self.m_updateTimer.setInterval(self.SPEED)
        self.m_updateTimer.timeout.connect(self.updateAngle)
        self.m_updateTimer.start()
        #旋转角度
        self.m_angle = 0
        self.m_outerRadius = 0
        #设置为无窗体
        self.setWindowFlags(Qt.FramelessWindowHint)
        #设置为背景透明
        self.setAttribute(Qt.WA_TranslucentBackground)

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        #设置为抗锯齿
        painter.setRenderHints(QPainter.Antialiasing|QPainter.HighQualityAntialiasing)
        #画外部圆
        self.drawUnderCircle(painter)
        #画BMW logo
        self.drawBMW(painter)

    def drawUnderCircle(self,painter):
        painter.save()
        #这里需要减4，不然上部分圆弧会出现平线
        self.m_outerRadius =(self.height() /2 - 4) if self.width() > self.height()else (self.width()/2 - 4)

        topLeft = QPointF(self.rect().center().x() - self.m_outerRadius,self.rect().center().y()-self.m_outerRadius)
        bottomRight = QPointF(self.rect().center().x()+ self.m_outerRadius,self.rect().center().y()+self.m_outerRadius)
        #大圆矩形
        circleRect = QRectF(topLeft,bottomRight)
        #不设置pen
        painter.setPen(Qt.NoPen);
        #设置渐变
        circleGradient = QRadialGradient(circleRect.center(),self.m_outerRadius,circleRect.center())
        circleGradient.setColorAt(0.0,self.OUTER_CIRCLE_START_COLOR)
        circleGradient.setColorAt(1.0,self.OUTER_CIRCLE_END_COLOR)
        painter.setBrush(circleGradient)
        #画圆
        painter.drawEllipse(circleRect)

        painter.restore()

    def drawBMW(self,painter):
        painter.save()

        # t = QTransform()
        #move to center
        # t.translate(self.rect().center().x(),self.rect().center().y())
        # #绕Z轴旋转
        # t.rotate(self.m_angle,Qt.ZAxis)
        # painter.setTransform(t)
        #上述代码效果与下面相同
        #move to center
        painter.translate(self.rect().center().x(),self.rect().center().y())
        painter.rotate(self.m_angle)
        #内半径
        innerRadius = float(self.m_outerRadius * self.RADIUS_FACTOR)
        topleft = QPointF(-innerRadius,-innerRadius)
        bottomRight = QPointF(innerRadius,innerRadius)
        tRect = QRectF(topleft,bottomRight)
        #这里需要考虑为什么乘以16,圆弧每个角度被分成16等分
        dAngle = float(90 * 16)
        startAngle = float(0)

        painter.setPen(Qt.NoPen)

        for angelIndex in range(4):
            pieGradient = QRadialGradient(tRect.center(), self.m_outerRadius, tRect.center())
            if angelIndex % 2 == 0: #蓝色
                pieGradient.setColorAt(0.0,self.BLUE_CIRCLE_START_COLOR)
                pieGradient.setColorAt(1.0,self.BLUE_CIRCLE_END_COLOR)

            else:
                pieGradient.setColorAt(0.0,self.WHITE_CIRCLE_START_COLOR)
                pieGradient.setColorAt(1.0,self.WHITE_CIRCLE_END_COLOR)

            painter.setBrush(pieGradient)
            painter.drawPie(tRect,startAngle,dAngle)

            startAngle += dAngle

        painter.restore()


    def updateAngle(self):
        self.m_angle += 1
        if self.m_angle > 360 :
            self.m_angle =0

        self.update()

    def sizeHint(self):
        return QSize(300,300)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mybmw = MyBMWWidget()
    mybmw.show()
    sys.exit(app.exec_())
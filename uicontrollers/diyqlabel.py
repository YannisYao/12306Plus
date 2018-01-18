'''
自定义点击出现图标的QLabel

author  yaoliang
date 20180118
'''

from  PyQt5.QtWidgets import QLabel,QApplication
from PyQt5 import QtCore,QtGui
from PyQt5.Qt import Qt
import sys
import uicontrollers.resources


class PaintQLabel(QLabel):

    def __init__(self,parent=None):
        """
        :param parent:
        """
        super(PaintQLabel, self).__init__(parent)
        self.points = []
        self.lastPoint = QtCore.QPoint(0,0)




    def paintEvent(self, QPaintEvent):
        super(PaintQLabel, self).paintEvent(QPaintEvent)
        if len(self.points) == 0:
            return;

        paint = QtGui.QPainter(self)
        pix = QtGui.QPixmap(':/images/selected.png')
        rects = self.transforRects()
        for rect in rects:
            paint.drawPixmap(rect,pix)
            
            
    def setPixmap(self, QPixmap):
        super(PaintQLabel, self).setPixmap(QPixmap)
        self.clearPoints()



    """def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.pressPoint = event.pos()



    def mouseMoveEvent(self, event):
        #鼠标左键按下同时移动鼠标
        if event.buttons() & Qt.LeftButton:
            self.movePoint = event.pos()"""


    def mouseReleaseEvent(self, event):
        #左鼠标释放
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            x = self.lastPoint.x()
            y = self.lastPoint.y()
            if x -18 > 0 and y - 30 > 0 :
                self.updatePoints()
                self.update()
            self.lastPoint = QtCore.QPoint(0,0)



    def updatePoints(self):
        """
        :return: 返回出现苗点的坐标
        """
        if len(self.points) == 0:
            self.points.append(self.lastPoint)
        else:
            self.refreshPoints()

    def refreshPoints(self):
        aPoint  =  self.lastPoint
        rects = self.transforRects()
        flag = False
        for i in range(len(rects)):
            if rects[i].contains(aPoint):
                self.points.pop(i)
                flag = True
        if not flag:
            self.points.append(aPoint)

    def transforRects(self):
        rects = []
        for point in self.points:
            rect = QtCore.QRect(point.x() - 18, point.y() - 18, 25, 25)
            rects.append(rect)
        return rects


    def sizeHint(self):
        return QtCore.QSize(293,190)

    def clearPoints(self):
        self.points = []
        self.lastPoint = QtCore.QPoint(0,0)
        self.update()

    def getPointXAndYs(self):
        abs = ''
        if len(self.points) == 0:
            return None
        else:
            for point in self.points:
                abs = abs + str(point.x())+','+ str(point.y())+','
            return abs.rstrip(',')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = PaintQLabel()
    label.setText("")
    label.setPixmap(QtGui.QPixmap(":/images/captcha.jpg"))
    label.setObjectName("label_captach")
    label.show()
    sys.exit(app.exec_())

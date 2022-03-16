import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPainter, QBrush

from Physics.vector import vector
from Physics.mover import Mover

from threading import Thread

import time

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)


class CWidget(QWidget):

    def __init__(self):
        super().__init__()

        #이동 물체
        self.mover = Mover()
        self.mover.location.x = self.width()/2
        self.mover.location.y = self.height()/2
        self.d = 20
        self.r = self.d/2

        self.thread = Thread(target=self.threadFunc)
        self.bThread = False

        self.initUI()

    def initUI(self):
        self.setWindowTitle('force')
        self.bThread = True
        self.thread.start()
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        rect = QRectF(self.mover.location.x-self.r, self.mover.location.y-self.r, self.d, self.d)
        qp.setBrush(self.mover.color)
        qp.drawEllipse(rect)
        qp.drawText(self.rect(), Qt.AlignTop|Qt.AlignLeft, '중력이 y방향으로 +0.1만큼 적용.')
        qp.end()

    def threadFunc(self):
        while self.bThread:

            gravity = vector(0.0, 0.1)
            self.mover.applyForce(gravity)

            self.mover.velocity += self.mover.acceleration
            self.mover.velocity.setLimit(10)
            self.mover.location += self.mover.velocity


            if self.mover.location.x+self.r > self.width():
                self.mover.location.x = self.width()-self.r
                self.mover.velocity.x *= -1
            elif self.mover.location.x-self.r < 0:
                self.mover.velocity.x *= -1
                self.mover.location.x = 0+self.r
            if self.mover.location.y+self.r > self.height():
                self.mover.location.y = self.height()-self.r
                self.mover.velocity.y *= -1
            elif self.mover.location.y-self.r < 0:
                self.mover.velocity.y *= -1
                self.mover.location.y = 0+self.r

            # 가속도를 0 설정
            # 뉴턴의 제1법칙(관성)에 따라 속도는 유지
            self.mover.acceleration*=vector(0,0)

            self.update()

            time.sleep(0.01)

    def closeEvent(self, e):
        self.bThread = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CWidget()
    sys.exit(app.exec_())

"""import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget
from PyQt5.QtCore import QDate


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        vbox = QVBoxLayout()
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())"""

"""import sys, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush, QPainterPath
from PyQt5.QtCore import Qt
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('QPainter를 이용한 그래픽스')
        self.show()
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        # 그리기 함수의 호출 부분
        qp.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())"""

"""def drawBezierCurve(self, qp):
    pen = QPen(Qt.black, 7)
    qp.setPen(pen)
    path = QPainterPath()
    path.moveTo(50, 50)
    path.cubicTo(200, 50, 50, 350, 350, 350)
     qp.drawPath(path)
    """
"""def drawBrushes(self, qp):
    brush = QBrush(Qt.SolidPattern)
    qp.setBrush(brush)
    qp.drawRect(20, 20, 110, 110)
    brush.setStyle(Qt.Dense1Pattern)
    qp.setBrush(brush)
    qp.drawRect(145, 20, 110, 110)
    brush.setStyle(Qt.Dense2Pattern)
    qp.setBrush(brush)
    qp.drawRect(270, 20, 110, 110)
    brush.setStyle(Qt.DiagCrossPattern)
    qp.setBrush(brush)
    qp.drawRect(20, 145, 110, 110)
    brush.setStyle(Qt.Dense5Pattern)
    qp.setBrush(brush)
    qp.drawRect(145, 145, 110, 110)
    brush.setStyle(Qt.Dense6Pattern)
    qp.setBrush(brush)
    qp.drawRect(270, 145, 110, 110)
    brush.setStyle(Qt.HorPattern)
    qp.setBrush(brush)
    qp.drawRect(20, 270, 110, 110)
    brush.setStyle(Qt.VerPattern)
    qp.setBrush(brush)
    qp.drawRect(145, 270, 110, 110)
    brush.setStyle(Qt.BDiagPattern)
    qp.setBrush(brush)
    qp.drawRect(270, 270, 110, 110)"""
"""import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())"""
"""import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('&Button1', self)
        btn1.setCheckable(True)
        btn1.toggle()

        btn2 = QPushButton(self)
        btn2.setText('Button&2')

        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())"""

""""#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, \
    QApplication, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 윈도우 설정
        self.setGeometry(300, 300, 400, 300)  # x, y, w, h
        self.setWindowTitle('Status Window')

        # QButton 위젯 생성 - FileDialog 을 띄위기 위한 버튼
        self.button = QPushButton('QFileDialog Open', self)
        self.button.clicked.connect(self.filedialog_open)
        self.button.setGeometry(10, 10, 200, 30)

        # 이미지를 추가할 라벨
        self.label = QLabel(self)

    def filedialog_open(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', '',
                                            'All File(*);; Image File(*.png *.jpg)')

        if fname[0]:
            # QPixmap 객체
            pixmap = QPixmap(fname[0])

            self.label.setPixmap(pixmap)  # 이미지 세팅
            self.label.setContentsMargins(10, 50, 10, 10)
            self.label.resize(pixmap.width(), pixmap.height())

            # 이미지의 크기에 맞게 Resize
            self.resize(pixmap.width(), pixmap.height())

        else:
            QMessageBox.about(self, 'Warning', '파일을 선택하지 않았습니다.')


    if __name__ == '__main__':
        app = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        sys.exit(app.exec_())"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout,QLabel
from PyQt5.QtGui import QPixmap


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pixmap = QPixmap('다운로드.jpg')

        self.label = QLabel(self)


        btn = QPushButton('show', self)

        btn.clicked.connect(self.showImage)


        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(btn)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def showImage(self):
        print("clicked")
        self.label.setPixmap(self.pixmap)  # 이미지 세팅
        self.label.setContentsMargins(10, 10, 10, 10)
        self.label.resize(self.pixmap.width(), self.pixmap.height())

        self.setWindowTitle('Show Image')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

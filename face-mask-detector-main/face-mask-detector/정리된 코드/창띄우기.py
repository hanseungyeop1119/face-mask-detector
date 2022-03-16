import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pixmap = QPixmap('mask.png')

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
        self.label.setPixmap(self.pixmap)
        self.label.setContentsMargins(10, 10, 10, 10)
        self.label.resize(self.pixmap.width(), self.pixmap.height())

        self.setWindowTitle('Show Image')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
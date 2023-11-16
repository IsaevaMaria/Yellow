import sys

from random import randint
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.drawCircle)
        self.f = False

    def drawCircle(self):
        self.f = True
        self.update()

    def paintEvent(self, event):
        if self.f:
            q = QPainter()
            q.begin(self)
            x, y =  randint(100, 150), randint(100, 150)
            r = randint(20, 80)
            q.setBrush(QColor(255, 204, 0))
            q.drawEllipse(100, 100, r, r)
            q.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
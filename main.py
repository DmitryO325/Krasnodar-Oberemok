import random
import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPainterPath
from PyQt5.QtWidgets import QWidget, QApplication


class Task(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()
        self.painter = QPainter()
        self.flag = False

    def initUI(self):
        self.pushButton.clicked.connect(self.make_circle)

    def paintEvent(self, event):
        if self.flag:
            self.painter.begin(self)
            self.draw()
            self.painter.end()
            self.flag = False

    def draw(self):
        size = random.randint(5, 200)
        self.painter.setBrush(QColor('yellow'))

        self.painter.drawEllipse(random.randint(0, 600), random.randint(100, 480), size, size)

    def make_circle(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    application = QApplication(sys.argv)
    example = Task()
    example.show()
    sys.exit(application.exec())

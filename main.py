import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainWindow

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.draw_circle)

    def draw_circle(self):
        self.ui.widget.update()

    def paintEvent(self, event):
        qp = QPainter(self.ui.widget)
        qp.setBrush(QColor("yellow"))
        diameter = random.randint(10, 100)
        x = random.randint(0, self.ui.widget.width() - diameter)
        y = random.randint(0, self.ui.widget.height() - diameter)
        qp.drawEllipse(x, y, diameter, diameter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec_())

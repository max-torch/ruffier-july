from PyQt5.QtCore import (
    QTimer,
    QTime,
    Qt
)
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit
)

import screen1 as scr1
import screen2 as scr2

def on_button_clicked():
    screen2.show()
    screen1.hide()
def on_button_clicked2():
    screen3.show()
    screen2.hide()


app = QApplication([])
screen1 = scr1.Screen1()
screen2 = scr2.Screen2()
screen1.button.clicked.connect(on_button_clicked)
screen2.result.clicked.connect(on_button_clicked2)

screen1.show()
app.exec_()
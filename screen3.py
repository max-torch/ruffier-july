from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout, 
    QLabel, 
    QPushButton
)

class Screen3(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Health Status Detection Application")
        self.setGeometry(100, 100, 1280, 720)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication([])
    window = Screen3()
    window.show()
    app.exec_()
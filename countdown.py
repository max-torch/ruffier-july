from PyQt5.QtCore import (
    QTimer,
    Qt,
    QTime
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

class countdown(QWidget):

    def __init__(self):
            
        def clicked():
            print("Button clicked")
            self.timer.start(1000)

        def start_countdown():
            print("Countdown started")
            # print the current time
            print(self.current_time.toString())
            self.current_time = self.current_time.addSecs(-1)

            self.label.setText(self.current_time.toString("mm:ss"))
            if self.current_time == QTime(0, 0):
                self.timer.stop()


        

        super().__init__()

        self.timer = QTimer(self)
        self.timer.timeout.connect(start_countdown)
        self.current_time = QTime(0, 1, 0) # current countdown time

        self.setWindowTitle("Countdown")
        self.setGeometry(100, 100, 1280, 720)

        self.layout = QVBoxLayout()
        self.label = QLabel("1:00")
        self.button = QPushButton("Start Countdown")

        self.layout.addWidget(self.label, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.button, alignment=Qt.AlignCenter)


        self.button.clicked.connect(clicked)

        self.setLayout(self.layout)
    


app = QApplication([])
window = countdown()
window.show()
app.exec_()
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

class Screen2(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Health Status Detection Application")
        self.setGeometry(100, 100, 1280, 720)
        self.layout = QHBoxLayout()
        self.layout2 = QVBoxLayout()
        self.layout3 = QVBoxLayout()

        self.label = QLabel("Enter your full name:")
        self.label2 = QLabel("Full years:")
        self.label3 = QLabel("""
Lie on your back and take your pulse for 15 seconds. Click the "Start first test" button to start the timer.
Write down the result in the appropriate field.
""")
        self.label4 = QLabel("""
Perform 30 squats in 45 seconds. To do this, click the "Start doing squats" button
to start the squat counter.
""")
        self.label5 = QLabel("""
Lie on your back and take your pulse for the first 15 seconds of the minute, then for the last 15 seconds of the minute.
Press the "Start final test" button to start the timer.
The seconds that should be measured are indicated in green and the minutes that should not be measured are indicated in black. Write down the results in the appropriate fields.
""")


        self.start_num = QLineEdit()
        self.start_num.setPlaceholderText("0")
        self.squat = QPushButton("Start doing squats")
        self.final = QPushButton("Start final test")
        self.final_num = QLineEdit()
        self.final_num.setPlaceholderText("0")
        self.final_num2 = QLineEdit()
        self.final_num2.setPlaceholderText("0")
        self.result = QPushButton("Send the results")

        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Full Name")
        self.input_year = QLineEdit()
        self.input_year.setPlaceholderText("0")
        self.start = QPushButton("Start first test")
        def clicked():
                self.timer.stop()
                self.timer.disconnect()
                self.current_time = QTime(0, 0, 15)
                self.countdown.setText(self.current_time.toString("hh:mm:ss"))
                self.timer.timeout.connect(start_countdown)
                self.timer.start(1000)



        def start_countdown():
                # print the current time
                print(self.current_time.toString())
                self.current_time = self.current_time.addSecs(-1)

                self.countdown.setText(self.current_time.toString("hh:mm:ss"))
                if self.current_time == QTime(0, 0, 0):
                        if self.countdown.text() == "00:00:00":  
                                self.timer.stop()

        self.timer = QTimer(self)
        self.timer.timeout.connect(start_countdown)
        self.current_time = QTime(0, 0, 15) # current countdown time

        self.countdown = QLabel("00:00:00")
        self.start.clicked.connect(clicked)

        self.layout2.addWidget(self.label, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.layout2.addWidget(self.input_name, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.layout2.addWidget(self.label2, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.layout2.addWidget(self.input_year, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.layout2.addWidget(self.label3, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.layout2.addWidget(self.start, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.layout2.addWidget(self.start_num, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.layout2.addWidget(self.label4, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.layout2.addWidget(self.squat, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.layout2.addWidget(self.label5, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.layout2.addWidget(self.final, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.layout2.addWidget(self.final_num, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.layout2.addWidget(self.final_num2, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.layout2.addWidget(self.result, alignment=Qt.AlignBottom | Qt.AlignCenter)
        self.layout3.addWidget(self.countdown, alignment=Qt.AlignRight | Qt.AlignCenter)
        
        self.layout.addLayout(self.layout2)
        self.layout.addLayout(self.layout3)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication([])
    window = Screen2()
    window.show()
    app.exec_()
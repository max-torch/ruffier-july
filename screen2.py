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

# -------------------------------------------------------------------------------------------------------------------------------

        def clicked():
                self.timer.stop()
                self.timer.disconnect()
                self.current_time = QTime(0, 0, 15)
                self.countdown.setText(self.current_time.toString("mm:ss"))
                self.timer.timeout.connect(start_countdown)
                self.timer.start(1000)
                self.countdown.setStyleSheet("color: white;")
        def clicked2():
                self.timer.stop()
                self.timer.disconnect()
                self.current_time = QTime(0, 0, 30)
                self.countdown.setText(self.current_time.toString("ss"))
                self.timer.timeout.connect(start_countdown2)
                self.timer.start(1500)
                self.countdown.setStyleSheet("color: white;")

        def clicked3():
                self.timer.stop()
                self.timer.disconnect()
                self.current_time = QTime(0, 1, 0)
                self.countdown.setText(self.current_time.toString("mm:ss"))
                self.timer.timeout.connect(start_countdown3)
                self.timer.start(1000)
                self.countdown.setStyleSheet("color: Chartreuse;")



        def start_countdown():
                # print the current time
                print(self.current_time.toString())
                self.current_time = self.current_time.addSecs(-1)

                self.countdown.setText(self.current_time.toString("mm:ss"))
                if self.current_time == QTime(0, 0, 0):
                        if self.countdown.text() == "00:00":  
                                self.timer.stop()
                        
        def start_countdown2():
                # print the current time
                print(self.current_time.toString())
                self.current_time = self.current_time.addSecs(-1)

                self.countdown.setText(self.current_time.toString("ss"))
                if self.current_time == QTime(0, 0, 0):
                        if self.countdown.text() == "00":  
                                self.timer.stop()
        def start_countdown3():
                # print the current time
                print(self.current_time.toString())
                self.current_time = self.current_time.addSecs(-1)

                self.countdown.setText(self.current_time.toString("mm:ss"))
                if self.current_time == QTime(0, 0, 0):
                        if self.countdown.text() == "00:00":  
                                self.timer.stop()
                if self.countdown.text() == "00:45":
                        self.countdown.setStyleSheet("color: white;")
                elif self.countdown.text() == "00:15":
                        self.countdown.setStyleSheet("color: Chartreuse;")

        
        self.timer = QTimer(self)
        self.timer.timeout.connect(start_countdown)

        self.countdown = QLabel("00:00")
        self.start.clicked.connect(clicked)
        self.squat.clicked.connect(clicked2)
        self.final.clicked.connect(clicked3)

# -------------------------------------------------------------------------------------------------------------------------------
        assessment = ''
        def resultclicked():
                self.name = self.input_name.text() 
                self.year = int(self.input_year.text())
                self.bp1 = int(self.start_num.text())
                self.bp2 = int(self.final_num.text())
                self.bp3 = int(self.final_num2.text())
                self.calc = (4 * (self.bp1 + self.bp2 + self.bp3) - 200) / 10
                print(self.name, self.year, self.bp1, self.bp2, self.bp3,)
                print(self.calc)
                if self.year in range(7, 9):
                        if self.calc >= 21:
                                assessment = "Low"
                        elif self.calc >= 17 and self.calc < 21:
                               assessment = "Satisfactory"
                        elif self.calc >= 12 and self.calc < 17:
                                assessment = "Average"
                        elif self.calc >= 6.5 and self.calc < 12:
                                assessment = "Above Average"
                        elif self.calc < 6.5:
                                assessment = "High"

                elif self.year in range(9, 11):
                        if self.calc >= 19.5:
                                assessment = "Low"
                        elif self.calc >= 15.5 and self.calc < 19.5:
                                assessment = "Satisfactory"
                        elif self.calc >= 10.5 and self.calc < 15.5:
                                assessment = "Average"
                        elif self.calc >= 5 and self.calc < 10.5:
                                assessment = "Above Average"
                        elif self.calc < 5:
                                assessment = "High"
                elif self.year in range(11, 13):
                        if self.calc >= 18:
                                assessment = "Low"
                        elif self.calc >= 14 and self.calc < 18:
                               assessment = "Satisfactory"
                        elif self.calc >= 9 and self.calc < 14:
                                assessment = "Average"
                        elif self.calc >= 3.5 and self.calc < 9:
                                assessment = "Above Average"
                        elif self.calc < 3.5:
                                assessment = "High"
                elif self.year in range(13, 15):
                        if self.calc >= 16.5:
                                assessment = "Low"
                        elif self.calc >= 12.5 and self.calc < 16.5:
                               assessment = "Satisfactory"
                        elif self.calc >= 7.5 and self.calc < 12.5:
                                assessment = "Average"
                        elif self.calc >= 2 and self.calc < 7.5:
                                assessment = "Above Average"
                        elif self.calc < 2:
                                assessment = "High"
                elif self.year >= 15:
                        if self.calc >= 15:
                                assessment = "Low"
                        elif self.calc >= 11 and self.calc < 15:
                               assessment = "Satisfactory"
                        elif self.calc >= 6 and self.calc < 11:
                                assessment = "Average"
                        elif self.calc >= 0.5 and self.calc < 6:
                                assessment = "Above Average"
                        elif self.calc < 0.5:
                                assessment = "High"
                self.countdown.setText(f"{assessment} {self.calc}")

        self.result.clicked.connect(resultclicked)

# -------------------------------------------------------------------------------------------------------------------------------


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
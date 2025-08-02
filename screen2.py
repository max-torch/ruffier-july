from PyQt5.QtCore import Qt
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
        layout = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        label = QLabel("Enter your full name:")
        label2 = QLabel("Full years:")
        label3 = QLabel("""
Lie on your back and take your pulse for 15 seconds. Click the "Start first test" button to start the timer.
Write down the result in the appropriate field.
""")
        label4 = QLabel("""
Perform 30 squats in 45 seconds. To do this, click the "Start doing squats" button
to start the squat counter.
""")
        label5 = QLabel("""
Lie on your back and take your pulse for the first 15 seconds of the minute, then for the last 15 seconds of the minute.
Press the "Start final test" button to start the timer.
The seconds that should be measured are indicated in green and the minutes that should not be measured are indicated in black. Write down the results in the appropriate fields.
""")

        input_name = QLineEdit()
        input_name.setPlaceholderText("Full Name")
        input_year = QLineEdit()
        input_year.setPlaceholderText("0")
        start = QPushButton("Start first test")
        countdown = QLabel("00:00:00")
        start_num = QLineEdit()
        start_num.setPlaceholderText("0")
        squat = QPushButton("Start doing squats")
        final = QPushButton("Start final test")
        final_num = QLineEdit()
        final_num.setPlaceholderText("0")
        final_num2 = QLineEdit()
        final_num2.setPlaceholderText("0")
        result = QPushButton("Send the results")
    

        layout2.addWidget(label, alignment=Qt.AlignLeft | Qt.AlignTop)
        layout2.addWidget(input_name, alignment=Qt.AlignLeft | Qt.AlignTop)
        layout2.addWidget(label2, alignment=Qt.AlignLeft | Qt.AlignTop)
        layout2.addWidget(input_year, alignment=Qt.AlignLeft | Qt.AlignTop)
        layout2.addWidget(label3, alignment=Qt.AlignLeft | Qt.AlignTop)
        layout2.addWidget(start, alignment=Qt.AlignLeft | Qt.AlignTop)
        layout2.addWidget(start_num, alignment=Qt.AlignLeft | Qt.AlignTop)
        layout2.addWidget(label4, alignment=Qt.AlignLeft | Qt.AlignTop)
        layout2.addWidget(squat, alignment=Qt.AlignLeft | Qt.AlignTop)
        layout2.addWidget(label5, alignment=Qt.AlignLeft | Qt.AlignTop)
        layout2.addWidget(final, alignment=Qt.AlignLeft | Qt.AlignTop)
        layout2.addWidget(final_num, alignment=Qt.AlignLeft | Qt.AlignTop)
        layout2.addWidget(final_num2, alignment=Qt.AlignLeft | Qt.AlignTop)
        layout2.addWidget(result, alignment=Qt.AlignBottom | Qt.AlignCenter)
        layout3.addWidget(countdown, alignment=Qt.AlignRight | Qt.AlignCenter)
        
        layout.addLayout(layout2)
        layout.addLayout(layout3)
        self.setLayout(layout)

app = QApplication([])
window = Screen2()
window.show()
app.exec_()
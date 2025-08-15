from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout, 
    QLabel, 
    QPushButton
)

class Screen1(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Health Status Detection Application")
        self.setGeometry(100, 100, 1280, 720)

        self.layout = QVBoxLayout()
        self.label = QLabel("Welcome to the Health status detection program!")
        self.paragraph = QLabel("""
This application allows you to use the Rufier test to make an initial diagnosis of your health.
The Rufier test is a set of physical exercises designed to assess your cardiac performance during physical exertion.
The subject lies in the supine position for 5 minutes and has their pulse rate measured for 15 seconds;
then, within 45 seconds, the subject performs 30 squats.
When the exercise ends, the subject lies down and their pulse is measured again for the first 15 seconds
and then for the last 15 seconds of the first minute of the recovery period.
Important! If you feel unwell during the test (dizziness
tinnitus, shortness of breath, etc.) stop the test and consult a physician.
""")
        self.button = QPushButton("Start")
        self.layout.addWidget(self.label, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.paragraph, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)
        
if __name__ == "__main__":
    app = QApplication([])
    window = Screen1()
    window.show()
    app.exec_()
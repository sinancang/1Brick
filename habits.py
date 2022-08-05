from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QPushButton

from popup import InputPopup


class HabitsFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        length = 600
        height = 380
        self.setObjectName("habitsWidget")
        self.setMinimumSize(length, height)
        self.setMaximumSize(length, height)
        self.setStyleSheet(open("StyleSheets/habitStyle.css").read())

        self.createButton()

    def createButton(self):
        self.button = QPushButton("Add", self)
        self.button.setObjectName("addButton")
        self.button.resize(50, 35)
        self.button.move(510, 30)
        self.button.setStyleSheet("background-color: #BC4A3C;")
        self.button.clicked.connect(self.queryPopup)
        self.button.setFont(QFont('Arial', 15))

    def queryPopup(self):
        self.query = InputPopup()

    def addHabit(self):
        habitEntry = '{ "date": "20220802", "habit": "Coding", "time": "1H" }'

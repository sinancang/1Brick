from PyQt5.QtWidgets import QFrame, QPushButton


class HabitsFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        length = 600
        height = 325
        self.setObjectName("habitsWidget")
        self.setMinimumSize(length, height)
        self.setMaximumSize(length, height)
        self.setStyleSheet(open("StyleSheets/habitStyle.css").read())

        # self.createButton()

    def createButton(self):
        self.button = QPushButton(self)
        self.layout().addWidget(self.button)

    def addHabit(self):
        habitEntry = '{ "date": "20220802", "habit": "Coding", "time": "1H" }'

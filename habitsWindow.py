from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QPushButton, QLabel, QScrollArea, QSizePolicy, QVBoxLayout, QGroupBox

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

        self.createHabitEntryArea()
        self.createButton()

    def createHabitEntryArea(self):
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setObjectName("habitsScrollArea")
        self.scrollArea.move(25, 50)
        self.scrollArea.resize(550, 305)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)

        groupBox = QGroupBox()
        self.scrollAreaLayout = QVBoxLayout()
        self.scrollAreaLayout.setObjectName("habitsScrollAreaLayout")
        groupBox.setLayout(self.scrollAreaLayout)
        self.scrollArea.setWidget(groupBox)

    def createButton(self):
        self.button = QPushButton("Add\nHabit", self)
        self.button.setObjectName("addButton")
        self.button.resize(50, 30)
        self.button.move(525, 15)
        self.button.clicked.connect(self.queryPopup)
        self.button.setFont(QFont('Arial', 15))

    def queryPopup(self):
        self.query = InputPopup()

    def showHabitEntry(self, habitName):
        habitEntry = QLabel()
        habitEntry.setStyleSheet("background-color: #BC4A3C;")
        habitEntry.setText(habitName)
        habitEntry.setMinimumHeight(50)
        habitEntry.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.scrollAreaLayout.addWidget(habitEntry)

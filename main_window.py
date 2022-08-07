import json

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

import utils
from calendarWindow import BrickCalendar
from habitsWindow import HabitsFrame
from ui_interface import UI_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI_MainWindow()
        self.ui.setupUI(self)
        self.show()
        self.createCalendar()
        self.calendar.raise_()

        self.create_habits_widget()
        self.habits.lower()
        self.displayHabitEntries()

    def createCalendar(self):
        self.calendar = BrickCalendar(self)
        self.ui.gridLayout.addWidget(self.calendar, 0, 0, 1, 1, Qt.AlignHCenter | Qt.AlignTop)

    def create_habits_widget(self):
        self.habits = HabitsFrame(self)
        self.ui.gridLayout.addWidget(self.habits, 0, 0, 1, 1, Qt.AlignHCenter | Qt.AlignBottom)

    def displayHabitEntries(self):
        with open('db/habitEntries.json') as f:
            if utils.is_empty(f):
                return

            habitEntries = json.load(f)

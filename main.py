import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import calendar
from ui_interface import UI_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI_MainWindow()
        self.ui.setupUI(self)
        self.show()
        self.createCalendar()
        self.create_habits_widget()

    def createCalendar(self):
        self.calendar = calendar.Scheduler(self)
        self.ui.gridLayout.addWidget(self.calendar, 0, 0, 1, 1, Qt.AlignHCenter | Qt.AlignTop)

    def create_habits_widget(self):
        self.habits = QFrame(self)
        self.ui.gridLayout.addWidget(self.habits, 0, 0, 1, 1, Qt.AlignHCenter | Qt.AlignBottom)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

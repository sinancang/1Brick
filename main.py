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

    def createCalendar(self):
        length = 600
        height = 400

        self.calendar = calendar.Scheduler(self)
        self.calendar.setObjectName(u"calendarWidget")
        self.calendar.setMinimumSize(QSize(length, height))
        self.calendar.setMaximumSize(length, height)
        self.calendar.setStyleSheet(open("calendarStyle.css").read())
        self.calendar.setGridVisible(True)

        self.ui.gridLayout.addWidget(self.calendar, 0, 0, 1, 1, Qt.AlignHCenter | Qt.AlignTop)

    def createHabits(selfs):
        length = 600
        height = 400

    def createNewWidget(self, rowNumber, columnNumber):
        self.frame = QFrame(self.ui.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(80, 80))
        self.frame.setMaximumSize(QSize(80, 80))
        self.frame.setStyleSheet(u"background-color: rgb(255, 212, 168);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.ui.gridLayout.addWidget(self.frame, rowNumber, columnNumber, 1, 1, Qt.AlignHCenter | Qt.AlignVCenter)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

import json

from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QFormLayout, QCheckBox, QHBoxLayout


class InputPopup(QWidget):
    def __init__(self, parent=None):
        super(InputPopup, self).__init__()
        self.initUI()

    def initUI(self):
        length = 400
        height = 150

        self.setMinimumSize(length, height)
        self.setMaximumSize(length, height)

        self.layout = QFormLayout(self)

        lineEdit1 = QLineEdit()
        label1 = QLabel("Habit Name:")
        self.layout.addRow(label1, lineEdit1)

        label2 = QLabel("Frequency:")
        buttonLayout = QHBoxLayout()
        self.addWeekdayButtons(buttonLayout)
        self.layout.addRow(label2)
        self.layout.addRow(buttonLayout)

        self.button = QPushButton()
        self.button.setText("Save")
        self.button.clicked.connect(lambda: self.addHabitEntry(lineEdit1.text()))
        self.layout.addRow(self.button)

        self.show()

    def addWeekdayButtons(self, buttonLayout):
        self.buttons = []
        self.checkedDays = {"Mon": False, "Tue": False, "Wed": False, "Thu": False,
                            "Fri": False, "Sat": False, "Sun": False}

        b1 = QCheckBox("Mon")
        b1.setObjectName("Mon")
        b1.stateChanged.connect(lambda: self.adjustCheckedDays(b1))
        self.buttons.append(b1)

        b2 = QCheckBox("Tue")
        b2.setObjectName("Tue")
        b2.stateChanged.connect(lambda: self.adjustCheckedDays(b2))
        self.buttons.append(b2)

        b3 = QCheckBox("Wed")
        b3.setObjectName("Wed")
        b3.stateChanged.connect(lambda: self.adjustCheckedDays(b3))
        self.buttons.append(b3)

        b4 = QCheckBox("Thu")
        b4.setObjectName("Thu")
        b4.stateChanged.connect(lambda: self.adjustCheckedDays(b4))
        self.buttons.append(b4)

        b5 = QCheckBox("Fri")
        b5.setObjectName("Fri")
        b5.stateChanged.connect(lambda: self.adjustCheckedDays(b5))
        self.buttons.append(b5)

        b6 = QCheckBox("Sat")
        b6.setObjectName("Sat")
        b6.stateChanged.connect(lambda: self.adjustCheckedDays(b6))
        self.buttons.append(b6)

        b7 = QCheckBox("Sun")
        b7.setObjectName("Sun")
        b7.stateChanged.connect(lambda: self.adjustCheckedDays(b7))
        self.buttons.append(b7)

        for button in self.buttons:
            buttonLayout.addWidget(button)
            button.setCheckable(True)

    def addHabitEntry(self, habitName):
        if not habitName:
            # display error message instead
            raise ValueError("Invalid value")
        entry = {'name': habitName, 'days': self.checkedDays}
        # load json, check if it's already there
        # Append entry to json
        print(json.dumps(entry))

        self.hide()

    def adjustCheckedDays(self, button):
        self.checkedDays[button.text()] = button.isChecked()

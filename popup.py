from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QFormLayout


class InputPopup(QWidget):
    def __init__(self, parent=None):
        super(InputPopup, self).__init__()
        self.initUI()

    def initUI(self):
        length = 200
        height = 100

        self.setMinimumSize(length, height)
        self.setMaximumSize(length, height)

        self.layout = QFormLayout(self)

        lineEdit = QLineEdit()
        label = QLabel("New Habit")
        self.layout.addRow(label, lineEdit)

        self.button = QPushButton()
        self.button.setText("Save")
        self.layout.addRow(self.button)

        self.show()

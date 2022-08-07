from PyQt5.QtWidgets import QMessageBox


def is_empty(file):
    firstChar = file.read(1)
    if not firstChar:
        return True

    file.seek(0)
    return False


def displayError(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Error")
    msg.setInformativeText(text)
    msg.setWindowTitle("Error")
    msg.exec_()

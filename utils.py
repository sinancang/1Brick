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


def intToDayOfWeekStr(int):
    if int == 1:
        return "Mon"
    elif int == 2:
        return "Tue"
    elif int == 3:
        return "Wed"
    elif int == 4:
        return "Thu"
    elif int == 5:
        return "Fri"
    elif int == 6:
        return "Sat"
    elif int == 7:
        return "Sun"

    raise ValueError

import sys

from PyQt5.QtWidgets import *

from mainWindow import MainWindow


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

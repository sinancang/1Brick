from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class UI_MainWindow(object):
    def setupUI(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 1200)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralWidget")

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(0, 0, 500, 400)

        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUI(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUI(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"1Brick", None))

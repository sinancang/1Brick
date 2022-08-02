from PyQt5.QtCore import QDate, Qt, QPoint
from PyQt5.QtWidgets import QCalendarWidget


class Scheduler(QCalendarWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        for d in (Qt.Saturday, Qt.Sunday,):
            fmt = self.weekdayTextFormat(d)
            fmt.setForeground(Qt.white)
            self.setWeekdayTextFormat(d, fmt)

        self.events = {
            QDate(2023, 3, 24): ["Sinan's birthday"],
            QDate(2023, 4, 6): ["Bengi's birthday"]
        }

    def paintCell(self, painter, rect, date):
        super().paintCell(painter, rect, date)
        if date in self.events:
            painter.setBrush(Qt.yellow)
            painter.drawEllipse(rect.topLeft() + QPoint(12, 7), 3, 3)

from PyQt5.QtGui import QMouseEvent
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QLineEdit, QTextEdit


class KLineEdit(QLineEdit):
    doubleClicked = pyqtSignal(QMouseEvent)

    def __init__(self, parent):
        super(KLineEdit, self).__init__(parent)
        self.setCursor(Qt.PointingHandCursor)
        # self.viewport().setCursor(Qt.PointingHandCursor)

    def mouseDoubleClickEvent(self, e: QMouseEvent):
        super(KLineEdit, self).mouseDoubleClickEvent(e)
        self.doubleClicked.emit(e)



class KTextEdit(QTextEdit):
    doubleClicked = pyqtSignal(QMouseEvent)

    def __init__(self, parent):
        super(KTextEdit, self).__init__(parent)
        self.setCursor(Qt.PointingHandCursor)
        self.viewport().setCursor(Qt.PointingHandCursor)

    def mouseDoubleClickEvent(self, e: QMouseEvent):
        super(KTextEdit, self).mouseDoubleClickEvent(e)
        self.doubleClicked.emit(e)

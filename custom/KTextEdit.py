from PyQt5.QtGui import QMouseEvent
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QLineEdit, QTextEdit


class KLineEdit(QLineEdit):
    simpleClicked = pyqtSignal(QMouseEvent)

    def __init__(self, parent):
        super(KLineEdit, self).__init__(parent)
        self.setCursor(Qt.PointingHandCursor)
        # self.viewport().setCursor(Qt.PointingHandCursor)

    def mouseReleaseEvent(self, e: QMouseEvent):
        super(KLineEdit, self).mouseReleaseEvent(e)
        self.simpleClicked.emit(e)


class KTextEdit(QTextEdit):
    simpleClicked = pyqtSignal(QMouseEvent)

    def __init__(self, parent):
        super(KTextEdit, self).__init__(parent)
        self.setCursor(Qt.PointingHandCursor)
        self.viewport().setCursor(Qt.PointingHandCursor)

    def mouseReleaseEvent(self, e: QMouseEvent):
        super(KTextEdit, self).mouseReleaseEvent(e)
        self.simpleClicked.emit(e)

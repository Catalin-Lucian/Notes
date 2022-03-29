from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont, QMouseEvent
from PyQt5.QtWidgets import QFrame, QSizePolicy

from colorsMod.ColorScheme import ColorScheme
from custom.KNoteWindow import KNoteWindow
from custom.KTextEdit import KLineEdit, KTextEdit
from data.noteData import NoteData


class KNote(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.colorScheme = ColorScheme()
        self.data = NoteData()

        self.titleText = KLineEdit(self)
        self.contentText = KTextEdit(self)

        self.noteWindow = KNoteWindow()

        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet(f"background-color: {self.colorScheme.colors['primary_color']};"
                           "border-radius: 15px; "
                           f"color:{self.colorScheme.colors['primary_text_color']};")
        self.setMinimumSize(QSize(260, 200))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.setSizePolicy(sizePolicy)
        self.setCursor(Qt.PointingHandCursor)

        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)

        self.titleText.setFont(font)
        self.titleText.setText(self.data.title)
        self.titleText.setReadOnly(True)
        self.titleText.setGeometry(16, 11, 501, 44)
        self.titleText.doubleClicked.connect(self.mouseDoubleClickEvent)

        font.setBold(False)
        font.setPointSize(14)
        self.contentText.setFont(font)
        self.contentText.setText(self.data.content)
        self.contentText.setReadOnly(True)
        self.contentText.setGeometry(16, 64, 501, 133)
        self.contentText.doubleClicked.connect(self.mouseDoubleClickEvent)
        self.contentText.setStyleSheet(f"background-color: {self.colorScheme.colors['primary_color']};"
                                       f"color:{self.colorScheme.colors['secondary_text_color']};")

        self.noteWindow.setNoteData(self.data)

    def mouseDoubleClickEvent(self, e: QMouseEvent):
        super(KNote, self).mouseDoubleClickEvent(e)
        if e.button() == Qt.LeftButton:
            self.noteWindow.show()

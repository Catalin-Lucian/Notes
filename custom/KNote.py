from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont, QMouseEvent
from PyQt5.QtWidgets import QFrame, QSizePolicy

from colorsMod.ColorScheme import ColorScheme
from custom.KNoteWindow import KNoteWindow
from custom.KTextEdit import KLineEdit, KTextEdit
from data.noteData import NoteData, SQLiteManager
from voice.voiceManger import VoiceManager


class KNote(QFrame):
    def __init__(self, parent=None, data=None):
        super().__init__(parent)
        self.colorScheme = ColorScheme()
        self.voice = VoiceManager()
        self.data = NoteData() if data is None else data

        self.sqlite = SQLiteManager()

        self.titleText = KLineEdit(self)
        self.contentText = KTextEdit(self)

        self.noteWindow = KNoteWindow()
        self.noteWindow.close_signal.connect(self.onNoteWindowClose)

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
        self.titleText.setPlaceholderText("Note title")
        self.titleText.simpleClicked.connect(self.mouseDoubleClickEvent)

        font.setBold(False)
        font.setPointSize(14)
        self.contentText.setFont(font)
        self.contentText.setHtml(self.data.content)
        self.contentText.setPlaceholderText("content here")
        self.contentText.setReadOnly(True)
        self.contentText.setGeometry(16, 64, 501, 133)
        self.contentText.simpleClicked.connect(self.mouseDoubleClickEvent)
        self.contentText.setStyleSheet(f"background-color: {self.colorScheme.colors['primary_color']};"
                                       f"color:{self.colorScheme.colors['secondary_text_color']};"
                                       "QScrollBar:vertical {"
                                       "width: 2px;"
                                       "margin: 45px 0 45px 0;}")
        # self.contentText.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.noteWindow.setNoteData(self.data)
        self.noteWindow.title.textChanged.connect(self.onTitleChanged)
        self.noteWindow.content.textChanged.connect(self.onContentChanged)

    def mouseReleaseEvent(self, e: QMouseEvent):
        super(KNote, self).mouseReleaseEvent(e)
        if e.button() == Qt.LeftButton:
            self.noteWindow.show()
            self.voice.sInsertTitle.connect(self.noteWindow.title.setText)
            self.voice.sInsertContent.connect(self.noteWindow.content.setHtml)

    def onTitleChanged(self):
        self.data.title = self.noteWindow.title.text()
        self.titleText.setText(self.data.title)

    def onContentChanged(self):
        self.data.content = self.noteWindow.content.toHtml()
        self.contentText.setHtml(self.data.content)

    def onNoteWindowClose(self):
        self.noteWindow.hide()
        self.sqlite.updateNote(self.data)

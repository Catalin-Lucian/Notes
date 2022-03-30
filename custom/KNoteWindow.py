from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QWidget, QLineEdit, QTextEdit, QFrame, QPushButton

from colorsMod.ColorScheme import ColorScheme
from data.noteData import NoteData
from voice.voiceManger import VoiceManager


class KNoteWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.colorScheme = ColorScheme()
        self.data = NoteData()

        self.centralWidget = QWidget(self)
        self.title = QLineEdit(self.centralWidget)
        self.content = QTextEdit(self.centralWidget)
        self.toolBar = QFrame(self.centralWidget)

        self.button = QPushButton(self.centralWidget)

        self.setup_ui()

    def setup_ui(self):
        self.resize(445, 550)
        self.setCentralWidget(self.centralWidget)
        self.setStyleSheet(f"background-color: {self.colorScheme.colors['primary_color_darker']};"
                           f"border-radius: 0")

        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)

        self.title.setGeometry(36, 60, 373, 44)
        self.title.setText(self.data.title)
        self.title.setFont(font)
        self.title.setPlaceholderText("Note title")
        self.title.setStyleSheet(f"background-color: {self.colorScheme.colors['primary_color_darker']};"
                                 f"color: {self.colorScheme.colors['primary_text_color']}")

        font.setBold(False)
        font.setPointSize(14)
        self.content.setGeometry(15, 118, 415, 380)
        self.content.setText(self.data.content)
        self.content.setFont(font)
        self.content.setPlaceholderText("content here")
        self.content.setStyleSheet(f"background-color: {self.colorScheme.colors['primary_color_darker']};"
                                   f"color: {self.colorScheme.colors['secondary_text_color']}")

        self.toolBar.setGeometry(15, 508, 415, 43)

    def setNoteData(self, noteData):
        self.data = noteData
        self.title.setText(self.data.title)
        self.content.setText(self.data.content)

    def processNewString(self, text):
        # self.content.setHtml(text)
        print(text)
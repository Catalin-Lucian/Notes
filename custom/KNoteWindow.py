from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton

from colorsMod.ColorScheme import ColorScheme
from data.noteData import NoteData
# from main import Notes


class KNoteWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.colorScheme = ColorScheme()
        self.data = NoteData()

        self.centralWidget = QWidget(self)
        self.button = QPushButton(self)
        # self.button.clicked.connect(Notes().show())

        self.setup_ui()

    def setup_ui(self):
        self.resize(445, 550)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setStyleSheet(f"background-color: {self.colorScheme.colors['primary_color_darker']};"
                                         f"border-radius: 0")

    def setNoteData(self, noteData):
        self.data = noteData

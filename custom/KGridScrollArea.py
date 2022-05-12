from PyQt5.QtCore import Qt
from PyQt5.QtGui import QResizeEvent
from PyQt5.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QFrame, QLayout

from custom.KNote import KNote
from data.noteData import NoteData, SQLiteManager


class KGridScrollArea(QScrollArea):
    def __init__(self, parent=None):
        super(KGridScrollArea, self).__init__(parent=parent)

        self.scrollAreaWidgetContents = QWidget()
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.spacerItem = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.sqlite = SQLiteManager()

        self.setup_ui()

    def setup_ui(self):
        self.setGeometry(20, 120, 550, 750)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())

        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(550, 750)
        self.setFrameShape(QFrame.NoFrame)
        self.setLineWidth(0)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setAlignment(Qt.AlignCenter)

        self.scrollAreaWidgetContents.setGeometry(0, 0, 550, 750)

        self.verticalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)

        self.verticalLayout.addSpacerItem(self.spacerItem)
        self.setWidget(self.scrollAreaWidgetContents)

        self.load_notes()

    def load_notes(self):
        notes = self.sqlite.getNotesList()
        # order by created
        notes.sort(key=lambda x: x.created, reverse=True)
        for note in notes:
            self.addWidget(KNote(data=note))

    def addWidget(self, widget: KNote):
        self.verticalLayout.removeItem(self.spacerItem)
        self.verticalLayout.addWidget(widget)
        self.verticalLayout.addItem(self.spacerItem)

    def removeWidget(self, widget: KNote):
        self.verticalLayout.removeWidget(widget)
        self.sqlite.deleteNote(widget.data.id)

    def insertWidget(self, index: int, widget: KNote):
        self.verticalLayout.insertWidget(index, widget)
        self.sqlite.addNote(widget.data)


import os
import sys
import threading
import time

import psutil as psutil
from PyQt5.QtCore import QSize, pyqtSignal
from PyQt5.QtGui import QFont, QResizeEvent
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QLabel, QPushButton

from colorsMod.ColorScheme import ColorScheme
from custom.KAudio import KAudio
from custom.KButton import KButton
from custom.KGridScrollArea import KGridScrollArea
from custom.KNote import KNote
from voice.voiceManger import VoiceManager


class Notes(QMainWindow):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Notes, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        super(Notes, self).__init__()

        self.colorScheme = ColorScheme()
        self.audio = KAudio()
        self.voice = VoiceManager()
        self.voiceThread = threading.Thread(target=self.voice.start)
        self.voiceThread.start()

        self.centralWidget = QWidget(self)

        self.contentArea = KGridScrollArea(self.centralWidget)
        self.contentArea.addWidget(KNote())
        self.contentArea.addWidget(KNote())

        self.addButton = KButton(self.centralWidget, "plus.png")
        self.searchButton = KButton(self.centralWidget, "search.png")
        self.settingsButton = KButton(self.centralWidget, "settings.png")

        # --------------------------------
        self.allButton = QLabel(self.centralWidget)
        self.allLine = QWidget(self.centralWidget)

        self.folderButton = QLabel(self.centralWidget)
        self.folderLine = QWidget(self.centralWidget)

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Notes")
        self.resize(590, 850)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setStyleSheet(f"background-color: {self.colorScheme.colors['primary_color_darker']};")

        self.addButton.setGeometry(525, 785, 54, 54)
        self.addButton.setIconSize(QSize(34, 34))
        self.addButton.setStyleSheet(f"background-color:{self.colorScheme.colors['secondary_color']};"
                                     f"border-radius: 25")
        self.addButton.click_signal.connect(self.addNewNote)

        self.searchButton.setGeometry(483, 41, 30, 30)
        self.searchButton.setIconSize(QSize(30, 30))

        self.settingsButton.setGeometry(540, 41, 30, 30)
        self.settingsButton.setIconSize(QSize(30, 30))
        self.settingsButton.sound = self.audio.shutterSound

        # ----------------------------------------------------
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setWeight(75)

        self.allButton.setGeometry(150, 102, 50, 26)
        self.allButton.setStyleSheet(f"color:{self.colorScheme.colors['accent_color']};"
                                     f"text-align: center")
        self.allButton.setText("All")
        self.allButton.setFont(font)

        self.allLine.setGeometry(140, 134, 50, 3)
        self.allLine.setStyleSheet(f"background-color:{self.colorScheme.colors['accent_color']}")

        self.folderButton.setGeometry(400, 102, 135, 26)
        self.folderButton.setStyleSheet(f"color:{self.colorScheme.colors['accent_color']};"
                                        f"text-align: center")
        self.folderButton.setText("Folder")
        self.folderButton.setFont(font)

        self.folderLine.setGeometry(414, 134, 50, 3)
        self.folderLine.setStyleSheet(f"background-color:{self.colorScheme.colors['accent_color']}")

        self.voice.sNewNote.connect(self.addNewNote)

    def closeEvent(self, event):
        self.audio.shutter()
        time.sleep(0.2)
        event.accept()

    def addNewNote(self):
        note = KNote()
        self.contentArea.addWidget(note)
        note.noteWindow.show()
        self.voice.sInsertTitle.connect(note.noteWindow.title.setText)
        self.voice.sInsertContent.connect(note.noteWindow.content.setHtml)
        note.noteWindow.button.clicked.connect(self.show)

    # def resizeEvent(self, event: QResizeEvent):
    #     super(Notes, self).resizeEvent(event)
    #     self.contentArea.resize(event.size())


def kill_proc_tree(pid, including_parent=True):
    parent = psutil.Process(pid)
    if including_parent:
        parent.kill()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    notes = Notes()

    notes.show()
    returnValue = app.exec()
    if returnValue is not None:
        kill_proc_tree(os.getpid())
        sys.exit(returnValue)

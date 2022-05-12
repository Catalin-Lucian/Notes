import os
import sys
import threading
import time

import psutil as psutil
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QLabel

from colorsMod.ColorScheme import ColorScheme
from custom.KAudio import KAudio
from custom.KButton import KButton
from custom.KCheckButton import KCheckButton
from custom.KGridScrollArea import KGridScrollArea
from custom.KNote import KNote
from video.VideoManager import VideoManager
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
        self.video = VideoManager()

        self.centralWidget = QWidget(self)
        self.contentArea = KGridScrollArea(self.centralWidget)

        self.addButton = KButton(self.centralWidget, "plus.png")
        self.searchButton = KButton(self.centralWidget, "search.png")

        self.voiceAssistButton = KCheckButton(self.centralWidget, "ai_disabled.svg", "ai_enabled.svg")
        self.voiceAssistThread = None

        self.videoMouseControlButton = KCheckButton(self.centralWidget, "cursor_disabled.svg", "cursor_enabled.svg")
        self.videoThread = None

        self.soundButton = KCheckButton(self.centralWidget, "sound_off.svg", "sound_on.svg")
        self.soundBool = False

        self.nameLabel = QLabel(self.centralWidget)

        self.setup_ui()

    def setup_ui(self):

        self.setWindowTitle("Notes")
        self.setFixedSize(590, 850)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setStyleSheet(f"background-color: {self.colorScheme.colors['primary_color_darker']};")

        self.addButton.setGeometry(525, 785, 54, 54)
        self.addButton.setIconSize(QSize(34, 34))
        self.addButton.setStyleSheet(f"background-color:{self.colorScheme.colors['secondary_color']};"
                                     f"border-radius: 25")
        self.addButton.click_signal.connect(self.addNewNote)

        self.searchButton.setGeometry(405, 41, 30, 30)
        self.searchButton.setIconSize(QSize(30, 30))

        self.videoMouseControlButton.setGeometry(451, 41, 30, 30)
        self.videoMouseControlButton.setIconSize(QSize(30, 30))
        self.videoMouseControlButton.check_signal.connect(self.activate_mouse_control)

        self.voiceAssistButton.setGeometry(503, 41, 30, 30)
        self.voiceAssistButton.setIconSize(QSize(30, 30))
        self.voiceAssistButton.check_signal.connect(self.activate_voice_assist)
        self.voiceAssistButton.sound = self.audio.shutterSound

        self.soundButton.setGeometry(548, 41, 30, 30)
        self.soundButton.setIconSize(QSize(30, 30))
        self.soundButton.check_signal.connect(self.activate_sound)

        # ----------------------------------------------------
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(28)
        font.setWeight(75)

        self.voice.sNewNote.connect(self.addNewNote)
        self.nameLabel.setGeometry(20, 41, 300, 35)
        self.nameLabel.setStyleSheet(f"color:{self.colorScheme.colors['accent_color']};"
                                     f"text-align: center")
        self.nameLabel.setText("Notes")
        self.nameLabel.setFont(font)

    def closeEvent(self, event):
        self.audio.shutter()
        time.sleep(0.2)
        event.accept()

    def addNewNote(self):
        note = KNote()
        self.contentArea.insertWidget(0, note)
        note.noteWindow.show()
        self.voice.sInsertTitle.connect(note.noteWindow.title.setText)
        self.voice.sInsertContent.connect(note.noteWindow.content.setHtml)
        note.noteWindow.button.clicked.connect(self.show)

    def activate_mouse_control(self, enable):
        if enable:
            self.videoThread = threading.Thread(target=self.video.start())
            self.videoThread.start()
        else:
            self.video.quitFlag = True

    def activate_sound(self, enable):
        self.audio.isOn = enable

    def activate_voice_assist(self, enable):
        if enable:
            self.voiceAssistThread = threading.Thread(target=self.voice.start)
            self.voiceAssistThread.start()
        else:
            self.voice.quitFlag = True

    # on close event
    def close(self):
        self.contentArea.saveNoteDataList()
        super(Notes, self).close()


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

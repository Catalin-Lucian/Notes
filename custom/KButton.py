import os

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtWidgets import QPushButton

from custom.KAudio import KAudio


class KButton(QPushButton):
    click_signal = pyqtSignal()

    def __init__(self, parent, iconUnClicked=None, iconClicked=None, iconHover=None):
        super(KButton, self).__init__(parent)

        self.audio = KAudio()

        self.clickedIcon = QIcon("icons\\" + iconClicked) if iconClicked else None
        self.unClickedIcon = QIcon("icons\\" + iconUnClicked) if iconUnClicked else None
        self.hoverIcon = QIcon("icons\\" + iconHover) if iconHover else None

        self.sound = None
        self.onTop = False

        self.setupUi()

    def setupUi(self):
        self.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.setText("")
        if self.unClickedIcon:
            self.setIcon(self.unClickedIcon)
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def mousePressEvent(self, e):
        super(KButton, self).mousePressEvent(e)
        if e.button() == Qt.LeftButton:
            if self.clickedIcon:
                self.setIcon(self.clickedIcon)

            # play audio if found or default tap sound
            if self.sound:
                self.audio.playSound(self.sound)
            else:
                self.audio.tap()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            if self.onTop:
                if self.hoverIcon:
                    self.setIcon(self.hoverIcon)
            else:
                if self.unClickedIcon:
                    self.setIcon(self.unClickedIcon)
            self.click_signal.emit()

    def enterEvent(self, e):
        super(KButton, self).enterEvent(e)
        self.onTop = True
        if self.hoverIcon:
            self.setIcon(self.hoverIcon)

    def leaveEvent(self, e):
        super(KButton, self).enterEvent(e)
        self.onTop = False
        if self.unClickedIcon:
            self.setIcon(self.unClickedIcon)

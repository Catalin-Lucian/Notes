import sys
import time

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QLabel, QPushButton

from colorsMod.ColorScheme import ColorScheme
from custom.KAudio import KAudio
from custom.KButton import KButton
from custom.KGridScrollArea import KGridScrollArea


class Notes(QMainWindow):
    def __init__(self):
        super(Notes, self).__init__()

        self.colorScheme = ColorScheme()
        self.audio = KAudio()

        self.centralWidget = QWidget(self)

        self.addButton = KButton(self.centralWidget, "plus.png")
        self.searchButton = KButton(self.centralWidget, "search.png")
        self.settingsButton = KButton(self.centralWidget, "settings.png")

        self.contentArea = KGridScrollArea(self.centralWidget)
        self.contentArea.addWidget(QPushButton())

        # --------------------------------
        self.allButton = QLabel(self.centralWidget)
        self.allLine = QWidget(self.centralWidget)

        self.folderButton = QLabel(self.centralWidget)
        self.folderLine = QWidget(self.centralWidget)

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Notes")
        self.resize(590, 900)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setStyleSheet(f"background-color: {self.colorScheme.colors['primary_color_darker']};")

        self.addButton.setGeometry(516, 826, 54, 54)
        self.addButton.setIconSize(QSize(34, 34))
        self.addButton.setStyleSheet(f"background-color:{self.colorScheme.colors['secondary_color']};"
                                     f"border-radius: 25")

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

    def closeEvent(self, event):
        self.audio.shutter()
        time.sleep(0.2)
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    notes = Notes()

    notes.show()
    sys.exit(app.exec())

import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QLabel

from colorsMod.ColorScheme import ColorScheme
from custom.KButton import KButton


class Notes(QMainWindow):
    def __init__(self):
        super(Notes, self).__init__()

        self.colorScheme = ColorScheme()

        self.centralWidget = QWidget(self)

        # self.card1 = QWidget(self.centralWidget)
        # self.card2 = QWidget(self.centralWidget)
        # self.card3 = QWidget(self.centralWidget)
        # self.card4 = QWidget(self.centralWidget)
        # self.card5 = QWidget(self.centralWidget)
        # self.card6 = QWidget(self.centralWidget)
        #
        # self.addButton = KButton(self.centralWidget, "plus.png")
        # self.searchButton = KButton(self.centralWidget, "search.png")
        # self.settingsButton = KButton(self.centralWidget, "settings.png")
        #
        # self.allButton = QLabel(self.centralWidget)
        # self.allLine = QWidget(self.centralWidget)
        #
        # self.folderButton = QLabel(self.centralWidget)
        # self.folderLine = QWidget(self.centralWidget)

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

        self.card1.setGeometry(34, 180, 260, 243)
        self.card1.setStyleSheet(f"background-color:{self.colorScheme.colors['primary_color']};"
                                 f"border-radius: 15")

        self.card2.setGeometry(309, 180, 260, 222)
        self.card2.setStyleSheet(f"background-color:{self.colorScheme.colors['primary_color']};"
                                 f"border-radius: 15")

        self.card3.setGeometry(34, 438, 260, 310)
        self.card3.setStyleSheet(f"background-color:{self.colorScheme.colors['primary_color']};"
                                 f"border-radius: 15")

        self.card4.setGeometry(309, 416, 260, 251)
        self.card4.setStyleSheet(f"background-color:{self.colorScheme.colors['primary_color']};"
                                 f"border-radius: 15")

        self.card5.setGeometry(34, 762, 260, 155)
        self.card5.setStyleSheet(f"background-color:{self.colorScheme.colors['primary_color']};"
                                 f"border-radius: 15")

        self.card6.setGeometry(309, 680, 260, 247)
        self.card6.setStyleSheet(f"background-color:{self.colorScheme.colors['primary_color']};"
                                 f"border-radius: 15")

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    notes = Notes()

    notes.show()
    sys.exit(app.exec())

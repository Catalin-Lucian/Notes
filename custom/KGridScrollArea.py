from PyQt5.QtCore import Qt
from PyQt5.QtGui import QResizeEvent
from PyQt5.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QFrame, QLayout

from custom.KNote import KNote


class KGridScrollArea(QScrollArea):
    def __init__(self, parent=None):
        super(KGridScrollArea, self).__init__(parent=parent)

        self.scrollAreaWidgetContents = QWidget()
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.spacerItem = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.setup_ui()

    def setup_ui(self):
        self.setGeometry(20, 163, 550, 687)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())

        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(550, 687)
        self.setFrameShape(QFrame.NoFrame)
        self.setLineWidth(0)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setAlignment(Qt.AlignCenter)

        self.scrollAreaWidgetContents.setGeometry(0, 0, 550, 687)

        self.verticalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)

        self.verticalLayout.addSpacerItem(self.spacerItem)

        self.setWidget(self.scrollAreaWidgetContents)

    def addWidget(self, widget: KNote):
        self.verticalLayout.removeItem(self.spacerItem)
        self.verticalLayout.addWidget(widget)
        self.verticalLayout.addItem(self.spacerItem)




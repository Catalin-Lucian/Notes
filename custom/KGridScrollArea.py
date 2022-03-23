from PyQt5.QtWidgets import QFrame, QHBoxLayout, QScrollArea, QWidget, QGridLayout


class KGridScrollArea(QFrame):
    def __init__(self, parent=None):
        super(KGridScrollArea, self).__init__(parent=parent)

        self.layout = QHBoxLayout(self)
        self.scrollArea = QScrollArea(self)
        self.scrollAreaWidgetContents = QWidget()
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)

    def setup_ui(self):
        self.setGeometry(20, 163, 550, 737)
        self.setStyleSheet("background-color: C4C4C4;")

        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layout.addWidget(self.scrollArea)

    def addWidget(self, widget):
        self.gridLayout.addWidget(widget)

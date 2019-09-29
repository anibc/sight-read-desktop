from PyQt5.QtWidgets import QWidget, QVBoxLayout
from sightread.ui.sheetwidget import SheetWidget

class SheetLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI( self ):
        self.rootLayout = QVBoxLayout()
        self.sw = SheetWidget()
        self.rootLayout.addWidget(self.sw)

        self.setLayout(self.rootLayout)

        self.setGeometry(60,60,1100,600)

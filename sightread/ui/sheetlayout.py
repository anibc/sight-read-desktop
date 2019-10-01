from PyQt5.QtWidgets import QWidget, QVBoxLayout
from sightread.ui.sheetwidget import SheetWidget
from sightread.ui.keyboardwidget import KeyboardWidget
from sightread.ui.visualizerwidget import VisualizerWidget
from sightread.ui.sheetlayoutcontroller import SheetLayoutController
from sightread.viewablenotes import NoteModel

class SheetLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.controller = SheetLayoutController(self)
        self.notes = NoteModel()

    def initUI( self ):
        self.rootLayout = QVBoxLayout()
        self.sw = SheetWidget()
        self.vw = VisualizerWidget()
        self.kw = KeyboardWidget()

        self.rootLayout.addWidget(self.sw)
        self.rootLayout.addWidget(self.vw)
        self.rootLayout.addWidget(self.kw)

        self.setLayout(self.rootLayout)

        self.setGeometry(60,60,1100,600)

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from sightread.ui.sheetwidget import SheetWidget
from sightread.ui.keyboardwidget import KeyboardWidget
from sightread.ui.waterfallwidget import WaterfallWidget
from sightread.ui.sheetlayoutcontroller import SheetLayoutController
from sightread.viewablenotes import NoteModel

class SheetLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = SheetLayoutController(self)
        self.notes = NoteModel()
        self.initUI()

    def initUI( self ):
        self.rootLayout = QVBoxLayout()
        self.sw = SheetWidget( self.notes )
        self.ww = WaterfallWidget( self.notes )
        self.kw = KeyboardWidget( self.notes )

        self.rootLayout.addWidget(self.sw)
        self.rootLayout.addWidget(self.ww)
        self.rootLayout.addWidget(self.kw)

        self.setLayout(self.rootLayout)

        self.setGeometry(60,60,1100,600)

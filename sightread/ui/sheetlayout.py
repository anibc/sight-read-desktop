from PyQt5.QtWidgets import QWidget, QVBoxLayout
from sightread.ui.sheetwidget import SheetWidget
from sightread.ui.keyboardwidget import KeyboardWidget
from sightread.ui.waterfallwidget import WaterfallWidget
from sightread.player.staticplayer import StaticPlayer

class SheetLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.player = StaticPlayer( self )
        self.initUI()

    def initUI( self ):
        self.rootLayout = QVBoxLayout()

        self.sw = SheetWidget( self.player )
        self.ww = WaterfallWidget( self.player )
        self.kw = KeyboardWidget( self.player )

        self.rootLayout.addWidget(self.sw)
        self.rootLayout.addWidget(self.ww)
        self.rootLayout.addWidget(self.kw)

        self.setLayout(self.rootLayout)

        self.setGeometry(60,60,1100,600)

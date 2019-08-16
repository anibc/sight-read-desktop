import sys
from PyQt5.QtWidgets import QApplication, QLabel
from sightread.ui.sheetwidget import SheetWidget

class App:
    def start( self ):
        app = QApplication(sys.argv)
        # mainWin = QLabel("hi")
        mainWin = SheetWidget()
        mainWin.show()
        sys.exit( app.exec_() )

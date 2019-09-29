import sys
from PyQt5.QtWidgets import QApplication, QLabel
from sightread.ui.sheetlayout import SheetLayout

class App:
    def start( self ):
        app = QApplication(sys.argv)
        # mainWin = QLabel("hi")
        mainWin = SheetLayout()
        mainWin.show()
        sys.exit( app.exec_() )

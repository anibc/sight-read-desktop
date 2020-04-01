import sys, logging
from PyQt5.QtWidgets import QApplication, QLabel
from sightread.ui.sheetlayout import SheetLayout

class App:
    def start( self ):
        self.initialize_logging()
        app = QApplication(sys.argv)
        # mainWin = QLabel("hi")
        mainWin = SheetLayout()
        mainWin.show()
        sys.exit( app.exec_() )
    def initialize_logging(self):
        logging.basicConfig(filename='app.log', format='%(asctime)s %(levelname)s: %(message)s', level=logging.DEBUG)


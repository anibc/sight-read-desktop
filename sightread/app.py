import sys, logging
from PyQt5.QtWidgets import QApplication, QLabel
from sightread.ui.sheetlayout import SheetLayout

class App:
    def start( self ):
        logger = self.initialize_logging()
        app = QApplication(sys.argv)
        # mainWin = QLabel("hi")
        mainWin = SheetLayout()
        mainWin.show()
        sys.exit( app.exec_() )
    def initialize_logging(self):
        form = logging.Formatter('%(asctime)s|%(levelname)s: %(message)s')
        hdlr = logging.FileHandler('logs/app.log')
        hdlr.setFormatter(form)
        logger = logging.getLogger('sightread')
        logger.addHandler(hdlr)
        logger.setLevel('DEBUG')
        logger.info("Logger sightread Configured")
        return logger


import sys
from PyQt5.QtWidgets import QApplication, QLabel

class App:
    def start( self ):
        app = QApplication(sys.argv)
        mainWin = QLabel("hi")
        mainWin.show()
        sys.exit( app.exec_() )

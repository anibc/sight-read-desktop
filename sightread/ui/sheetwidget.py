from PyQt5.QtWidgets import QWidget
import PyQt5.QtGui as QtGui

class SheetWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI( self ):
        pass

    def paintEvent( self, e ):
        qp = QtGui.QPainter()
        qp.begin( self )
        self.drawWidget(qp)
        qp.end()

    def drawWidget( self, qp ):
        qp.setPen(QtGui.QColor(255, 150, 150))
        qp.setBrush(QtGui.QColor(150, 255, 150))
        for i in range( 5 ):
            qp.drawLine( i * 10 + 50, 20, i * 10 + 50, 50 )

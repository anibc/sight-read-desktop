from PyQt5.QtWidgets import QWidget
import PyQt5.QtGui as QtGui
from sightread import mode
from sightread.midi.input import MIDIListener, register, deregister

class SheetWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._controller = None
        self.initUI()

    @property
    def controller( self ):
        return self._controller

    @controller.setter
    def controller( self, value ):
        if self._controller != None:
            deregister( self._controller )
        self._controller = value
        register( self._controller )

    def initUI( self ):
        self.mode = mode.MiniRandom( self )

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

class SheetController():
    def __init__( self, sw ):
        self.sw = sw
        sw.controller = self

class StaticSheet( SheetController, MIDIListener ):
    def on_midi_input( self, msg ):
        pass

class DynamicSheet( SheetController, MIDIListener ):
    def on_midi_input( self, msg ):
        pass

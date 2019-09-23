from PyQt5.QtWidgets import QWidget
import PyQt5.QtGui as QtGui
from sightread import mode
from sightread.midi.input import MIDIListener, register, deregister
from sightread import note

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
        width = self.size().width()
        height = self.size().height()
        qp.drawText(40,40, "Line of Text")
        # qp.drawGlyphRun();
        # dist_between_lines = dist_between_notes * 2 + 1
        dist_from_top = 10
        dist_between_notes = 5
        middle_gap = dist_between_notes * 5
        middle_c_n8 = note.MIDDLEC.n8 # 40
        for i in range( note.SHEETLOW.n8, note.SHEETHIGH.n8 + 1, 2 ):
            y = i * ( dist_between_notes + 1 ) + dist_from_top
            if i == middle_c_n8:
                y += middle_gap
            elif i > middle_c_n8:
                y += middle_gap * 2
            qp.drawLine( 0, y, width, y)

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

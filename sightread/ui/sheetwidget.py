from PyQt5.QtWidgets import QWidget
import PyQt5.QtGui as QtGui
from sightread import mode
from sightread.midi.input import MIDIListener, register, deregister
from sightread import note

# dist_between_lines = dist_between_notes * 2 + 1
dist_from_top = 10
dist_between_notes = 5
middle_gap = dist_between_notes * 5
middle_c_n8 = note.MIDDLEC.n8 # 40

class SheetWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.notes = {}
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
        # qp.setBrush(QtGui.QColor(150, 255, 150))
        # qp.setFont(QtGui.QFont('Arial', 30))
        # qp.drawText(40,40, "Line of Text")
        # qp.drawGlyphRun();
        self.draw_static_lines( qp )
        # self.draw_note_lines( qp, self.notes ) #TODO
        # self.draw_notes( qp, self.notes ) #TODO

    def draw_static_lines( self, qp ):
        qp.setPen(QtGui.QColor(10, 10, 10))
        width = self.size().width()
        for i in range( note.SHEETLOW.n8, note.SHEETHIGH.n8 + 1, 2 ):
            y = self.height_from_n8( i )
            qp.drawLine( 0, y, width, y)

    def height_from_note( self, n ):
        return height_from_n8( n.n8 )

    def height_from_n8( self, n8 ):
        y = n8 * ( dist_between_notes + 1 ) + dist_from_top
        if n8 == middle_c_n8:
            y += middle_gap
        elif n8 > middle_c_n8:
            y += middle_gap * 2
        return y

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

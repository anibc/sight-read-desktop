from PyQt5.QtWidgets import QWidget
import PyQt5.QtGui as QtGui
from sightread import mode
from sightread.midi.input import MIDIListener, register, deregister
from sightread import note

# dist_between_lines = dist_between_notes * 2 + 1
dist_from_top = 0
dist_between_notes = 5
middle_gap = dist_between_notes * 5
middle_c_n8 = note.MIDDLEC.n8 # 40

class SheetWidget(QWidget):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.initUI()

    def initUI( self ):
        self.setMinimumHeight( self.height_from_note( note.Note( note.SHEETLOW.n - 5 ) ) ) # TODO: derive exact required height from dist_between_notes

    def paintEvent( self, e ):
        qp = QtGui.QPainter()
        qp.begin( self )
        self.drawWidget(qp)
        qp.end()

    def drawWidget( self, qp ):
        qp.setPen(QtGui.QColor(255, 150, 150))
        # qp.setBrush(QtGui.QColor(150, 255, 150))
        # qp.setFont(QtGui.QFont('Arial', 30))
        # qp.drawText(40,40, str(self.size().width()) )
        # qp.drawGlyphRun();
        self.draw_static_lines( qp )
        self.draw_note_lines( qp )
        self.draw_notes( qp )

    def draw_static_lines( self, qp ):
        qp.setPen(QtGui.QColor(10, 10, 10))
        width = self.size().width()
        for i in range( note.SHEETLOW.n8, note.SHEETHIGH.n8 + 1, 2 ):
            y = self.height_from_n8( i )
            qp.drawLine( 0, y, width, y)

    def draw_note_lines( self, qp ):
        self.draw_top_note_lines( qp )
        self.draw_bottom_note_lines( qp )

    def draw_top_note_lines( self, qp ):
        pass

    def draw_bottom_note_lines( self, qp ):
        pass

    def draw_note( self, qp, n ):
        y = self.height_from_note( n ) + 6 #qp.fontInfo().pixelSize() // 8
        qp.drawText( 80 + ( n.st - self.player.curtime ) * 10, y, u'\U0001D15D')
        if not n.isWhite():
            qp.drawText( 80 + ( n.st - self.player.curtime ) * 10 - 10, y, u'\U0001D12C')

    def draw_notes( self, qp ):
        # https://unicode-table.com/en/blocks/musical-symbols/
        # qp.drawText(40,40, u'\u266D')
        # qp.drawText(48,40, u'\U0001D15D')
        # return NotImplemented
        qp.setFont( QtGui.QFont("Times", 30) )
        width = self.size().width()
        for n in self.player.tracknotes.rangeST( self.player.curtime, self.player.curtime + width / 10):
            self.draw_note( qp, n )
        for n in self.player.playednotes.rangeST(0,width / 10):
            y = self.height_from_note( n ) + 6 #qp.fontInfo().pixelSize() // 8
            qp.drawText( 80 + n.st * 10, y, u'\U0001D15D')
            if not n.isWhite():
                qp.drawText( 80 + ( n.st - self.player.curtime ) * 10 - 10, y, u'\U0001D12C')

    def height_from_note( self, n ):
        return self.height_from_n8( n.n8 )

    def height_from_n8( self, n8 ):
        y = ( 120 - n8 ) * ( dist_between_notes + 1 ) + dist_from_top
        if n8 == middle_c_n8:
            y += middle_gap
        elif n8 < middle_c_n8:
            y += middle_gap * 2
        return y

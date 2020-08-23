import logging
from PyQt5.QtWidgets import QWidget
import PyQt5.QtGui as QtGui
from sightread import mode
from sightread.midi.input import MIDIListener, register, deregister
from sightread import note
from sightread.viewablenotes import ViewableNote

# dist_between_lines = dist_between_notes * 2 + 1
dist_from_top = 50
dist_from_bottom = 50
dist_between_notes = 5
middle_gap = dist_between_notes * 5
middle_c_n8 = note.MIDDLEC.n8  # 40


class SheetWidget(QWidget):
    def __init__(self, player):
        super().__init__()
        self.logger = logging.getLogger(__name__)
        self.top_offset = 0
        self.player = player
        self.initUI()
        self.logger.info("SheetWidget initialized")
        # logging.info('works?')

    def initUI(self):
        self.update_ranges()
        min_note = note.Note(
            min(
                [
                    self.tracknotesrange.minNote.n,
                    # self.playednotesrange.minNote.n,
                    note.SHEETLOW.n,
                ]
            )
        )
        max_note = note.Note(
            max(
                [
                    self.tracknotesrange.maxNote.n,
                    # self.playednotesrange.maxNote.n,
                    note.SHEETHIGH.n,
                ]
            )
        )
        self.top_offset = self.height_from_note(max_note) - dist_from_top
        self.setMinimumHeight(
            dist_from_top
            + dist_from_bottom
            + abs(self.height_from_note(max_note) - self.height_from_note(min_note))
        )

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()

    def drawWidget(self, qp):
        qp.setPen(QtGui.QColor(255, 150, 150))
        # qp.setBrush(QtGui.QColor(150, 255, 150))
        # qp.setFont(QtGui.QFont('Arial', 30))
        # qp.drawText(40,40, str(self.size().width()) )
        # qp.drawGlyphRun();
        self.update_ranges()
        self.draw_static_lines(qp)
        self.draw_note_lines(qp)
        self.draw_notes(qp)

    def update_ranges(self):
        self.leftx = self.player.curtime - 150
        self.rightx = self.leftx + self.size().width() - 150
        self.playednotesrange = self.player.playednotes
        # self.playednotesrange = self.player.playednotes.range(
        #     0, self.righttime - self.lefttime
        # )
        self.tracknotesrange = self.player.tracknotes.range(
            self.leftx, self.rightx
        )

    def draw_static_lines(self, qp):
        qp.setPen(QtGui.QColor(10, 10, 10))
        width = self.size().width()
        for i in range(note.SHEETLOW.n8, note.SHEETHIGH.n8 + 1, 2):
            y = self.height_from_n8(i)
            qp.drawLine(0, y, width, y)

    def draw_note_lines(self, qp):
        self.draw_top_note_lines(qp)
        self.draw_bottom_note_lines(qp)

    def draw_top_note_lines(self, qp):
        pass

    def draw_bottom_note_lines(self, qp):
        pass

    def draw_note(self, qp, vn):
        y = self.height_from_note(vn) + 6  # qp.fontInfo().pixelSize() // 8
        qp.drawText(80 + vn.x, y, u"\U0001D15D")
        if not vn.isWhite():
            qp.drawText(80 + vn.x - 10, y, u"\U0001D12C")

    def draw_notes(self, qp):
        # https://unicode-table.com/en/blocks/musical-symbols/
        qp.setFont(QtGui.QFont("Times", 30))
        width = self.size().width()
        for vn in self.tracknotesrange.l:
            self.draw_note(qp, vn)
        playedVns = []
        for n in self.playednotesrange:
            playedVns.append(ViewableNote(n, 20))
        for vn in playedVns:
            self.draw_note(qp, vn)

    def height_from_note(self, n, top_offset=None):
        return self.height_from_n8(n.n8, top_offset)

    def height_from_n8(self, n8, top_offset=None):
        if top_offset == None:
            top_offset = self.top_offset
        y = (120 - n8) * (dist_between_notes + 1) + dist_from_top - top_offset
        if n8 == middle_c_n8:
            y += middle_gap
        elif n8 < middle_c_n8:
            y += middle_gap * 2
        return y

import mido, random, logging
from PyQt5.QtCore import QTimer
import sightread.midi.input as midiinput
from sightread.viewablenotes import ViewableNote, NoteModel
from sightread.player import Player
from sightread import note


class DynamicPlayer(Player, midiinput.MIDIListener):
    def __init__(self, sl):
        self.logger = logging.getLogger(__name__)
        self.sl = sl
        self.tracknotes = NoteModel(TwoHandWhiteRandGen())
        self.playednotes = NoteModel()
        self.curtime = 0
        self._bpm = 10
        self.timer = self.initQTimer()
        midiinput.register(self)
        # midiname = next( ( n for n in mido.get_input_names() if 'V61' in n ) )
        # self.midi_input = mido.open_input( midiname, callback=self.midi_callback )

    @property
    def bpm(self):
        return self._bpm

    @bpm.setter
    def bpm(self, value):
        pvalue = _bpm
        self.curtime = self.curtime / value * pvalue
        self._bpm = value

    def initQTimer(self):
        qt = QTimer()
        qt.setTimerType(0) # PreciseTimer
        qt.setInterval(16)
        qt.timeout.connect(self.timerTimeout)
        return qt

    def timerTimeout(self):
        elapsed = self.timer.interval() / 1000
        self.curtime += elapsed
        # self.logger.info("timer elapsed, curtime: " + str(self.curtime))
        pass

    def play(self):
        self.timer.start()

    def pause(self):
        self.timer.stop()

    def stop(self):
        self.curtime = -3
        self.pause()

    def on_midi_input(self, msg):
        print(msg)
        if msg.type == "note_on":
            self.playednotes.insert(ViewableNote(msg.note, 0, 10))
            left = list(
                filter(lambda n: n.st == self.tracknotes.l[0].st, self.tracknotes.l)
            )
            if all(
                (
                    i in set([n.n for n in self.playednotes.l])
                    for i in set([n.n for n in left])
                )
            ):
                self.curtime += 10
                for n in left:
                    self.tracknotes.remove(n)
        elif msg.type == "note_off":
            self.playednotes.l = list(
                filter(lambda n: n.n != msg.note, self.playednotes.l)
            )
        self.sl.update()
        print("midi event picked up")


def OneHandWhiteRandGen():
    i = 0
    while True:
        i += 10
        n = random.randrange(note.SHEETLOW.n, note.SHEETHIGH.n)
        yield (ViewableNote(note.Note(n).white(), i, i + 10))


def TwoHandWhiteRandGen():
    i = 0
    while True:
        i += 10
        n = random.randrange(note.SHEETLOW.n, note.SHEETHIGH.n)
        m = random.randrange(note.SHEETLOW.n, note.SHEETHIGH.n - 1)
        if m == n:
            m += 1
        yield (
            ViewableNote(note.Note(n), i, i + 10),
            ViewableNote(note.Note(m), i, i + 10),
        )

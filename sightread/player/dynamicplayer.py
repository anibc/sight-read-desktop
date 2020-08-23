import mido, random, logging
from PyQt5.QtCore import QTimer
import sightread.midi.input as midiinput
from sightread.viewablenotes import ViewableNote
from sightread.notemodel import NoteModel
from sightread.player import Player
from sightread import note

FPS = 20

class DynamicPlayer(Player, midiinput.MIDIListener):
    def __init__(self, sl):
        self.logger = logging.getLogger(__name__)
        self.sl = sl
        self.tracknotes = NoteModel()
        self.playednotes = set()
        self.curtime = 0
        self._bpm = 10
        self.timer = self.initQTimer()
        midiinput.register(self)

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
        qt.setInterval(1000//FPS)
        qt.timeout.connect(self.timerTimeout)
        return qt

    def timerTimeout(self):
        elapsed = self.timer.interval() / 1000
        self.curtime += elapsed
        # self.logger.info("timer elapsed, curtime: " + str(self.curtime))
        self.sl.update()

    def play(self):
        self.timer.start()

    def pause(self):
        self.timer.stop()

    def stop(self):
        self.curtime = -3
        self.pause()

    def on_midi_input(self, msg):
        if msg.type == "note_on":
            self.playednotes.add(msg.note)
        elif msg.type == "note_off":
            self.playednotes.remove(msg.note)
        else:
            return
        self.sl.update()




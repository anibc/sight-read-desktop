import mido, random, logging
from PyQt5.QtCore import QTimer
import sightread.midi.input as midiinput
from sightread.note.viewablenotes import ViewableNote
from sightread.note.model import NoteModel, XPerBeat
from sightread.player import Player
from sightread import note

FPS = 20
MinBPM = 10
BPMInc = 1
ACCMS = 500
ACC = ACCMS / 1000


class DynamicPlayer(Player, midiinput.MIDIListener):
    def __init__(self, sl):
        self.logger = logging.getLogger(__name__)
        self.sl = sl
        self.tracknotes = NoteModel(self.OneHandWhiteRandGen, addClump=self.addClump)
        self.playednotes = set()
        self.curtime = 0
        self._bpm = 20  # MinBPM
        self.timer = self.initQTimer()
        self.secondTimer = self.initSecondQTimer()
        self.clumps = []
        self.score = []  # last ten
        midiinput.register(self)

    @property
    def bpm(self):
        return self._bpm

    @bpm.setter
    def bpm(self, value):
        pvalue = self._bpm
        self.curtime = self.curtime / value * pvalue
        self._bpm = value

    def initQTimer(self):
        qt = QTimer()
        qt.setTimerType(0)  # PreciseTimer
        qt.setInterval(1000 // FPS)
        qt.timeout.connect(self.timerTimeout)
        return qt

    def timerTimeout(self):
        elapsed = self.timer.interval() / 1000
        self.curtime += elapsed
        # self.logger.info("timer elapsed, curtime: " + str(self.curtime))
        self.sl.update()

    def initSecondQTimer(self):
        qt = QTimer()
        qt.setTimerType(0)  # PreciseTimer
        qt.setInterval(1000)
        qt.timeout.connect(self.secondTimerTimeout)
        return qt

    def secondTimerTimeout(self):
        # self.bpm += 1
        # while True:
        #     last = self.tracknotes.measures.last
        #     if (
        #         last * (1 + XPerBeat) + self.tracknotes.measures[last].lastX()
        #         < self.tracknotes.timeToX(self.curtime, self.bpm)
        #         + self.sl.sw.size().width()
        #     ):
        #         self.logger.debug("Adding vn")
        #         gen = OneHandWhiteRandGen()
        #         self.tracknotes.appendNextBeat(next(gen))
        #     else:
        #         break
        pass

    def play(self):
        self.timer.start()
        self.secondTimer.start()

    def pause(self):
        self.timer.stop()
        self.secondTimer.stop()

    def stop(self):
        self.curtime = -3
        self.pause()

    def addClump(self, clumpNotes, x):
        self.clumps.append((x, clumpNotes))

    def updateScore(self):
        hitTime = self.curtime  # calc more precisely
        leftx = self.tracknotes.timeToX(hitTime - ACC, self.bpm)
        rightx = self.tracknotes.timeToX(hitTime + ACC, self.bpm)
        clumps = self.clumps
        self.clumps = []
        for clump in clumps:
            if clump[0] < leftx:
                self.score.append(False)
            elif clump[0] > rightx:
                self.clumps.append(clump)
            else:
                match = self.playednotes == {n.n for n in clump[1]}
                if match:
                    self.score.append(True)
                else:
                    self.clumps.append(clump)
        self.score = self.score[-10:]
        scstr = ["True" if x else "False" for x in self.score]
        self.logger.debug(" ".join(scstr))

    def on_midi_input(self, msg):
        if msg.type == "note_on":
            self.playednotes.add(msg.note)
            self.updateScore()
        elif msg.type == "note_off" and msg.note in self.playednotes:
            self.playednotes.remove(msg.note)
        else:
            return
        self.sl.update()

    def OneHandWhiteRandGen(self):
        while True:
            n = random.randrange(note.SHEETLOW.n, note.SHEETHIGH.n)
            # yield (note.Note(n).white(),)
            yield (note.MIDDLEC,)

import logging
from sightread.note.notefreq import NoteFreq
from sightread.note.drawablenote import DrawableNote
from sightread.note.notesview import NotesView

class TimeSignature:
    def __init__(self, beats=4, beatType=4):
        self.beats = beats
        self.beatType = beatType

# make not scrollable for transient scores
class Score():
    def __init__(self, timeSig):
        self.logger = logging.getLogger(__name__)
        self.notes = dict() # key: Unique ID, val: Note
        self.timeSig = timesig
        self.measures = []
        return NotImplemented
    def tryLoadUpto(x):
        return NotImplemented
    def timeToX(self, time, bps):
        return NotImplemented
    def xToTime(self, x, bps):
        return NotImplemented
    def getNotesInRange(self, l, r):
        #TODO improve on naive implementation
        ret = []
        for note in self.notes.values():
            if l < note.x + note.xduration and r > note.x:
                ret.append(note)
        return sorted(ret)
    def barlines(self, l, r):
        #TODO improve on naive implementation
        ret = []
        if l <= 0 <= r:
            ret.append(0)
        for m in self.measures:
            end = m.startgx + m.width
            if l <= end <= r:
                ret.append(end)
        return ret

class Measure():
    def __init__(self, id_, startgx, width):
        self.id_ = id_
        self.startgx = startgx
        self.width = width
        self.notes = []
    def insert(self, note):
        self.notes.append(note)

class Note():
    def __init__(self, x, xduration, n, measure, gradingInfo=None):
        self.x = x
        self.xduration = xduration
        self.n = n
        self.measure = measure
        self.gradingInfo = gradingInfo



from sightread.note import Note
from sightread.note.viewablenotes import ViewableNote, ViewableNotesRange

XPerBeat = 50  # x axis separation value per beat


class Measure:
    def __init__(self):
        self.l = []

    def lastX(self):
        if len(self.l) < 1:
            return 0
        return self.l[-1].x

    def append(self, note):
        if note.x < self.lastX():
            raise ValueError
        self.l.append(note)


EmptyMeasure = Measure()


class MeasureList:
    def __init__(self, transient=False, capacity=20):
        self.transient = transient
        self.capacity = capacity
        self.l = list()
        self.r = list()
        self.first = 0
        self.last = 0
        self.l.append(Measure())

    def __getitem__(self, key):
        key = int(key)
        if self.first <= key <= self.last:
            if self.transient:
                if key - self.first < len(self.l):
                    return self.l[len(self.l) - 1 - key + self.first]
                return self.r[key - self.first - len(self.l)]
            else:
                if key >= 0 and key < len(self.l):
                    return self.l[key]
        return EmptyMeasure

    def __setitem__(self, key, value):
        raise NotImplemented

    def append(self, measure):
        self.last += 1
        if self.transient:
            self.r.append(measure)
            if len(self.l) + len(self.r) > self.capacity:
                self.first += 1
                if len(self.l) > 0:
                    self.l.pop()
                else:
                    while len(self.r) > 1:
                        self.l.append(self.r.pop())
                    self.r.pop()
        else:
            self.l.append(measure)


class TimeSignature:
    def __init__(self, beats=4, beatType=4):
        self.beats = beats
        self.beatType = beatType


class NoteModel:
    def __init__(self, source, timesig=TimeSignature(), transient=False, addClump=None):
        self.source = source
        self.measures = MeasureList(transient)
        self.timesignature = timesig
        self.logger = logging.getLogger(__name__)
        self.addClump = addClump

    def timeToX(self, time, bpm):
        "maps time for given bpm to x in NoteModel"
        beats = self.timesignature.beats
        width = beats * XPerBeat
        fullWidth = width + XPerBeat
        bps = bpm / 60
        b = time * bps
        measure = int(b // beats)
        b -= measure * beats
        lastXInMeasure = self.measures[measure].lastX()
        xInMeasure = b / beats * width
        prevX = measure * fullWidth + XPerBeat
        # self.logger.debug(
        #     "b: {}, measure: {}, lastXInMeasure: {}, xInMeasure: {}, prevX: {}".format(
        #         b, measure, lastXInMeasure, xInMeasure, prevX
        #     )
        # )
        if xInMeasure < lastXInMeasure:
            return prevX + xInMeasure
        xInMeasure -= lastXInMeasure
        xInMeasure /= width - lastXInMeasure
        xInMeasure *= width - lastXInMeasure + XPerBeat
        xInMeasure += lastXInMeasure
        return prevX + xInMeasure

    def xToTime(self, x, bpm):
        "maps x to time for given bpm in NoteModel"
        raise NotImplemented

    def range(self, l, r):
        "returns NoteRange from x value l to x value r"
        if self.lastX() <= r:
            for notes in self.source():
                self.appendNextBeat(notes)
                if self.lastX() > r:
                    break
        lst = []
        for m in range(
            int(l // ((1 + self.timesignature.beats) * XPerBeat)),
            int(2 + r // ((1 + self.timesignature.beats) * XPerBeat)),
        ):
            for vn in self.measures[m].l:
                if l <= vn.x + m * (1 + self.timesignature.beats) * XPerBeat <= r:
                    vn = ViewableNote(
                        vn.n, vn.x + m * (1 + self.timesignature.beats) * XPerBeat
                    )
                    lst.append(vn)
        return ViewableNotesRange(lst, l, r)

    def barlines(self, l, r):
        "returns list of x values at which bar lines must be drawn"
        ret = []
        width = (1 + self.timesignature.beats) * XPerBeat
        x = l // width
        while x <= r:
            if x >= l:
                ret.append(x)
            x += width
        return ret

    def lastX(self):
        lastm = self.measures.last
        return (1 + self.timesignature.beats) * XPerBeat * lastm + self.measures[
            lastm
        ].lastX()

    def appendNextBeat(self, notes):
        "appends note as viewablenote in next available beat"
        lastm = self.measures.last
        lastx = self.measures[lastm].lastX()
        # self.logger.debug("lastm: {}, lastx: {}".format(lastm, lastx))
        if lastm == 0 and len(self.measures[lastm].l) == 0:
            if self.addClump != None:
                self.addClump(notes, 0)
            for note in notes:
                self.measures[lastm].append(ViewableNote(note, lastx))
        elif lastx < 3 * XPerBeat:
            if self.addClump != None:
                self.addClump(notes, self.lastX() + XPerBeat)
            for note in notes:
                self.measures[lastm].append(ViewableNote(note, lastx + XPerBeat))
        else:
            self.measures.append(Measure())
            lastm += 1
            if self.addClump != None:
                self.addClump(notes, self.lastX())
            for note in notes:
                self.measures[lastm].append(ViewableNote(note, 0))

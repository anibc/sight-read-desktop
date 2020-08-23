from sightread.note import Note
from sightread.viewablenotes import *

XPerBeat = 50 # x axis separation value per beat

EmptyMeasure = Measure()

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

class MeasureList:
    def __init__(self, transient=false, capacity=20):
        self.transient = transient
        self.capacity = capacity
        self.l = list()
        self.r = list()
        self.first = 0
        self.last = 0
        self.l.append(Measure())

    def __getitem__(self, key):
        if transient:
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
        if transient:
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
    def __init__(self, timesig=TimeSignature(), transient=false):
        self._measures = MeasureList(transient)
        self.timesignature = timesig

    @property
    def measures(self):
        return _measures

    def timeToX(self, time, bpm):
        "maps time for given bpm to x in NoteModel"
        beats = self.timesignature.beats
        width = beats * XPerBeat
        fullWidth = width + XPerBeat
        bps = bpm / 60
        b = time * bps
        measure = b // beats
        b -= measure * beats
        lastXInMeasure = self.measures[measure].lastX
        xInMeasure = b / width
        prevX = measure * fullWidth + XPerBeat
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
        lst = []
        for m in range(l // ((1+self.timesignature.beats)*XPerBeat), 2 + r // ((1+self.timesignature.beats)*XPerBeat)):
            for vn in self.measures[m].l:
                if l <= vn.x <= r:
                    vn = ViewableNote(vn.n, vn.x + m * (1+self.timesignature.beats) * XPerBeat)
                    lst.append(vn)
        return NoteRange(lst, l, r)

    def barlines(self, l, r):
        "returns list of x values at which bar lines must be drawn"
        ret = []
        width = (1+self.timesignature.beats) * XPerBeat
        x = l // width
        while x <= r:
            if x >= l:
                ret.append(x)
                x += width
        return ret

    def appendNextBeat(self, note):
        "appends note as viewablenote in next available beat"
        lastm = self.measures.last
        lastx = self.measures[lastm].lastX()
        if len(self.measures[lastm]) > 0 and lastx < 3 * XPerBeat:
            self.measures[lastm].append(ViewableNote(note, lastx + XPerBeat))
        self.measures.append(Measure())
        lastm += 1
        self.measures[lastm].append(ViewableNote(note, 0))


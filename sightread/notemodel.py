from sightread.note import Note
from sightread.viewablenotes import *

XPerBeat = 50 # x axis separation value per beat


class TimeSignature:
    def __init__(self, beats=4, beatType=4):
        self.beats = beats
        self.beatType = beatType

class NoteModel:
    def __init__(self, timesig=TimeSignature()):
        self.timesignature = timesig

    @property
    def measures(self):
        raise NotImplemented

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
        raise NotImplemented

    def barlines(self, l, r):
        "returns list of x values at which bar lines must be drawn"
        raise NotImplemented

    def appendNextBeat(self):
        "appends note as viewablenote in next available beat"
        raise NotImplemented

class TransientNoteModel(NoteModel):
    pass

class ImmanentNoteModel(NoteModel):
    pass

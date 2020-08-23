from sightread.note import Note
from sightread.viewablenotes import *

XPerBeat = 50 # x axis separation value per beat


class TimeSignature:
    def __init__(self, beats=4, beatType=4):
        self.beats = beats
        self.beatType = beatType

class NoteModel:
    def __init__(self, timesig=TimeSignature()):
        self.measures = []
        self.timesignature = timesig

    def timeToX(self, time, bpm):
        "maps time in given bpm to x for NoteModel"
        pass

    def range(self, l, r):
        "returns NoteRange from x value l to x value r"
        pass
    
    def appendNextBeat(self):
        "appends note as viewablenote in next available beat"
        pass

class TransientNoteModel(NoteModel):
    pass

class ImmanentNoteModel(NoteModel):
    pass

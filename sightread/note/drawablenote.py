from sightread.note.notefreq import NoteFreq

class DrawableNote(NoteFreq):
    def __init__(self, notesView, n, x, noteLength, finger=None):  # x is relative to sheet start (not measure start)
        if type(n) == Note:
            super().__init__(n.n)
        else:
            super().__init__(n)
        self.notesView = notesView
        self.x = x
        self.noteLength = noteLength
        self.finger = finger

    @property
    def startTime():
        return NotImplemented
        self.notesView.score.xToTime(self.x, self.notesView.bpm)

    @property
    def duration():
        """from xduration"""
        return NotImplemented

    @property
    def durationType():
        """
            derive from xduration(closest approximation)
            1 = whole, 2 = half, 4 = quarter...
        """
        #TODO
        return 4

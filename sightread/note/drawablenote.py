from sightread.note.notefreq import NoteFreq


class DrawableNote(NoteFreq):
    def __init__(self, score, n, x, noteLength, finger=None):  # x is relative to sheet start (not measure start)
        if type(n) == Note:
            super().__init__(n.n)
        else:
            super().__init__(n)
        self.score = score
        self.x = x
        self.noteLength = noteLength
        self.finger = finger

    @property
    def startTime():
        return NotImplemented
        self.score.xToTime(self.x, self.score.player.bpm)

    @property
    def duration():
        """from xduration"""
        return NotImplemented


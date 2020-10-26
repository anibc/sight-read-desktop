class NotesView():
    def __init__(self, score, fromX, toX, curX, bps, activeNotes=set()):
        self.score = score
        self.timeSig = self.score.timeSig
        self.keySig = self.score.keySig
        self.fromX = fromX
        self.toX = toX
        self.curX = curX
        self.bps = bps
        self.activeNotes = activeNotes # note_on exists before fromX (notes still playing)
    def seek(self, fromX, toX):
        """adjust current with bbst from self.score"""
        return NotImplemented
    def drawableNotes(self):
        """yield in order of time, note_off first, NoteFreq"""
        return NotImplemented

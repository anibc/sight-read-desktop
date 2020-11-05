class NotesView():
    def __init__(self, score, fromX, toX, curX, bps):
        self.score = score
        self.timeSig = self.score.timeSig
        self.keySig = self.score.keySig
        self.activeNotes = set() # note_on exists before fromX (notes still playing)
        self.fromX = float("-inf")
        self.toX = float("-inf")
        self.seek(fromX, toX)
        self.bps = bps
        self.curX = curX
    def seek(self, fromX, toX):
        """adjust current with bbst from self.score"""
        return NotImplemented
    def drawableNotes(self):
        """yield in order of time, note_off first, NoteFreq"""
        return NotImplemented

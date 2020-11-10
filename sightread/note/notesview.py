class NotesView():
    def __init__(self, score, fromX, toX, curX, bps):
        self.score = score
        self.timeSig = self.score.timeSig
        self.keySig = self.score.keySig
        self.activeNotes = set() # note_on exists before fromX (notes still playing)
        self._drawableNotes = []
        self.fromX = float("-inf")
        self.toX = float("-inf")
        self.seek(fromX, toX)
        self.bps = bps
        self.curX = curX
        self.highestNote = None
        self.lowestNote = None
    def seek(self, fromX, toX):
        """adjust current with bbst from self.score"""
        return NotImplemented
    def drawableNotes(self):
        """yield in order of time, note_off first, NoteFreq"""
        for dn in self._drawableNotes:
            yield dn

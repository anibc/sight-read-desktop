class NotesView():
    def __init__(self, score, fromX, toX, curX, bps):
        self.score = score
        self.timeSig = self.score.timeSig
        self.keySig = self.score.keySig
        self.fromX = fromX
        self.toX = toX
        self.curX = curX
        self.bps = bps

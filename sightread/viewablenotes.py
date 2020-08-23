from sightread.note import Note

class ViewableNote(Note):
    def __init__(self, n, x): #x is relative to sheet start (not measure start)
        if type(n) == Note:
            super().__init__(n.n)
        else:
            super().__init__(n)
        self.x = x


class ViewableNotesRange:
    def __init__(self, l, st, et):
        self.l = l
        self.sx = sx
        self.ex = ex
        self.maxNote = (
            Note(max((i.n for i in l))) if len(l) else ViewableNote(Note(60), 0, 10)
        )
        self.minNote = (
            Note(min((i.n for i in l))) if len(l) else ViewableNote(Note(60), 0, 10)
        )
        self.l.sort(key=lambda x: x.x)



""" MIDI note object """
notes = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]


class NoteFreq:
    def __init__(self, v):
        if type(v) == int:
            self.n = v
        else:
            self.s = v

    @property
    def n(self):
        """ returns note in MIDI value format """
        return self._n

    @n.setter
    def n(self, value):
        """ sets from MIDI value format """
        self._n = value

    @property
    def s(self):
        mod = notes[self.n % 12]
        div = self.n // 12
        return str(div) + mod

    @s.setter
    def s(self, value):
        ind = -2 if value[-2].isalpha() else -1
        first, second = value[:ind], value[ind:]
        mod = notes.index(second)
        self.n = int(first) * 12 + mod

    @property
    def n8(self):
        """ map [0,2,4,5,7,9,11] to [0-6] """
        n = self.white().n
        div = n // 12
        mod = n % 12
        mod -= mod // 2
        return div * 7 + mod

    @n8.setter
    def n8(self, value):
        div = value // 7
        mod = value % 7
        self._n = div * 12 + 2 * mod - (mod + 1) // 4

    def isWhite(self):
        return self.s[-1] != "b"

    def white(self):
        return self if self.isWhite() else Note(self.n + 1)


LOW = NoteFreq(0)
HIGH = NoteFreq(180)
MIDDLEC = NoteFreq(60)
LOW88 = NoteFreq(9)
SHEETHIGH = NoteFreq(77)
SHEETLOW = NoteFreq(43)


def main():
    n = NoteFreq("5C")
    print("NoteFreq('5C').n =", n.n)
    n = NoteFreq(60)
    print("NoteFreq(60).s =", n.s)


if __name__ == "__main__":
    main()

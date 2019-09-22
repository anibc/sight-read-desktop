""" MIDI note object """
notes = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'] 

LOW  = Note( 0 )
HIGH = Note( 180 )
MIDDLEC = Note( 60 )
LOW88 = Note( 9 )
SHEETHIGH = Note( 77 )
SHEETLOW = Note( 43 )

class Note:
    def __init__( self, v ):
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
        mod = notes[ self.n % 12 ]
        div = self.n // 12 + 1
        return str(div) + mod
    @s.setter
    def s(self, value):
        ind = -2 if value[ -2 ].isalpha() else -1
        first, second = value[ :ind ], value[ ind: ]
        mod = notes.index( second )
        self.n = int( first ) * 12 + mod
    def isWhite( self ):
        return self.s[ -1 ] != 'b'
    def white( self ):
        return self if self.isWhite() else Note( self.n + 1 )

def main():
    n = Note('5C')
    print( "Note('5C').n =", n.n )
    n = Note(60)
    print( "Note(60).s =", n.s )

if __name__ == '__main__':
    main()

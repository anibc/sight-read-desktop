from sightread.note import Note
class ViewableNote( Note ):
    def __init__( self, n, t ):
        super().__init__()
        self.t = t
class NoteModel:
    def __init__( self ):
        self.l = []
    def insert( self, vn ):
        pass
    def remove( self, vn ):
        # only to be used by static controller
        pass
    def range( self, l, r ):
        """ generates ViewableNotes from time l to r """
        l, r = self.rangeIndeces( l, r )
        for i in range(l, r):
            yield self.l[ i ]

    def rangeIndeces( self, l, r ):
        m = 1
        while m <= len(self.l):
            m *= 2
        m //= 2

        i, j = -1, -1
        while m > 0:
            if i + m < len(self.l) and self.l[ i + m ].t < l:
                i += m
            if j + m < len(self.l) and self.l[ j + m ].t > r:
                j += m
            m //= 2
        return i + 1, j - 1

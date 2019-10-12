from sightread.note import Note
class ViewableNote( Note ):
    def __init__( self, n, st, et ):
        super().__init__( n.n )
        self.st = st
        self.et = et

class NoteModel:
    def __init__( self ):
        self.l = []
        self.incoming  = MinHeap( lambda n: n.st )
        self.windowIn  = MaxHeap( lambda n: n.st )
        self.windowOut = MinHeap( lambda n: n.et )
        self.outgoing  = MaxHeap( lambda n: n.et )
    def insert( self, vn ):
        # TODO implement with heap
        self.l.append( vn )
    def remove( self, vn ):
        # only to be used by static controller
        # TODO implement with heap
        self.l.remove(vn)
    def update( self, vn ):
        # TODO implement with heap
        self.l.sort(key= lambda vn: vn.et)
    def rangeET( self, l, r ):
        # TODO implement with heap
        """ generates ViewableNotes from time l to r """
        self.l.sort( key = lambda vn: vn.et )
        for vn in self.l:
            if vn.st <= r and vn.et >= l:
                yield vn
    def rangeST( self, l, r ):
        # TODO implement with heap
        """ generates ViewableNotes from time l to r """
        self.l.sort( key = lambda vn: vn.st )
        for vn in self.l:
            if vn.st <= r and vn.et >= l:
                yield vn

class Heap:
    def __init__( self, key ):
        self.key = key
        self.l = []
        self.k = {}
    def insert( self, n ):
        pass
    def remove( self, n ):
        pass
    def top( self, n ):
        pass
    def pop( self, n ):
        pass

class MinHeap(Heap):
    def cmp( self, a, b ):
        return self.key( a ) < self.key( b )

class MaxHeap(Heap):
    def cmp( self, a, b ):
        return self.key( a ) > self.key( b )


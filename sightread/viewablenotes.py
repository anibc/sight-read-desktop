from sightread.note import Note
class ViewableNote( Note ):
    def __init__( self, n, st, et ):
        if type(n) == Note:
            super().__init__( n.n )
        else:
            super().__init__( n )
        self.st = st
        self.et = et

class ViewableNotesRange():
    def __init__( self, l, st, et ):
        self.l = l
        self.st = st
        self.et = et
        self.maxNote = max(( i.n for i in l ))
        self.minNote = min(( i.n for i in l ))
        self.stIndex = list(range(len(l)))
        self.stIndex.sort( key = lambda x: self.l.st )
        self.etIndex = list(range(len(l)))
        self.etIndex.sort( key = lambda x: self.l.et )

    def SortedBySt( self ):
        return [ l[ i ] for i in stIndex ]

    def SortedByEt( self ):
        return [ l[ i ] for i in etIndex ]

class NoteModel:
    def __init__( self, nextnote=None ):
        self.l = []
        self.maxSt = -1
        self.nextnote = nextnote
        # self.incoming  = MinHeap( lambda n: n.st )
        # self.windowIn  = MaxHeap( lambda n: n.st )
        # self.windowOut = MinHeap( lambda n: n.et )
        # self.outgoing  = MaxHeap( lambda n: n.et )

        # self.insert( ViewableNote( Note( 60 ), 0, 10 ) )
        # self.insert( ViewableNote( Note( 56 ), 10, 20 ) )
        # self.insert( ViewableNote( Note( 65 ), 20, 30 ) )
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
    def range( self, l, r ):
        #TODO implement with heap
        """ generates ViewableNotes from time l to r """
        while r >= self.maxSt:
            if self.nextnote != None:
                try:
                    a = next( self.nextnote )
                    for vn in a:
                        self.l.append( vn )
                        self.maxSt = vn.st
                except e:
                    break
        return ViewableNotesRange( list( ( vn for vn in self.l if vn.st <= r and vn.et >= l ) ) )

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


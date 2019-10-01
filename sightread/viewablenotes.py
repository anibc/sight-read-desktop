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
        pass

import mido
from sightread.viewablenotes import ViewableNote, NoteModel

#TODO define interface for Player class using ABC module

class Player:
    pass

class StaticPlayer( Player ):
    def __init__( self, sl ):
        self.sl = sl
        self.tracknotes = NoteModel()
        self.playednotes = NoteModel()
        midiname = next( ( n for n in mido.get_input_names() if 'V61' in n ) )
        self.midi_input = mido.open_input( midiname, callback=self.midi_callback )

    def midi_callback( self, msg ):
        st = 10 + list(self.playednotes.rangeST(0,100000))[-1].st
        self.playednotes.insert( ViewableNote( msg.note, st, st + 10 ) )
        self.sl.update()
        print('midi event picked up')

import mido
from sightread.viewablenotes import ViewableNote, NoteModel
from sightread.player import Player
from sightread import note
import random

class StaticPlayer( Player ):
    def __init__( self, sl ):
        self.sl = sl
        self.tracknotes = NoteModel( OneHandWhiteRandGen() )
        self.playednotes = NoteModel()
        self.curtime = 0
        midiname = next( ( n for n in mido.get_input_names() if 'V61' in n ) )
        self.midi_input = mido.open_input( midiname, callback=self.midi_callback )

    def midi_callback( self, msg ):
        #st = 10 + list(self.playednotes.rangeST(0,100000))[-1].st
        print( msg )
        if msg.type == 'note_on':
            self.playednotes.insert( ViewableNote( msg.note, 0, 10 ) )
            left = list( filter( lambda n: n.st == self.tracknotes.l[ 0 ].st, self.tracknotes.l ) )
            if all( ( i in set( [ n.n for n in self.playednotes.l ] ) for i in set( [ n.n for n in left ] ) ) ):
                # self.curtime = left[ 0 ].st + 1
                self.curtime += 10
                for n in left:
                    self.tracknotes.remove( n )
        elif msg.type == 'note_off':
            self.playednotes.l = list( filter( lambda n: n.n != msg.note, self.playednotes.l ) )
        self.sl.update()
        print('midi event picked up')

def OneHandWhiteRandGen():
    i = 0
    while True:
        i += 10
        n = random.randrange( note.SHEETLOW.n, note.SHEETHIGH.n )
        yield ViewableNote( note.Note( n ).white(), i, i + 10 )

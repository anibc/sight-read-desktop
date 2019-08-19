from sightread import midi
from sightread.ui import sheetwidget
class MiniRandom( midi.input.MIDIListener ):
    def __init__( self, sw ):
        self.sw = sheetwidget.StaticSheetWidget( sw )
        midi.input.register( self )
    def on_midi_input( self, msg ):
        pass

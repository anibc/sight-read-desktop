import mido

def main():
    print( "starting" )
    mfile = mido.MidiFile('mfile.mid')
    for i, track in enumerate(mfile.tracks):
        print( i, track.name )
        for msg in mfile:
            print( msg)
    print( "went past" )

main()

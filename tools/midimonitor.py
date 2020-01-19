import mido

def main():
    print( "starting" )
    keyboard = mido.get_input_names()[ 1 ]
    with mido.open_input( keyboard ) as inp:
        for m in inp:
            print( m )
    print( "went past" )

main()

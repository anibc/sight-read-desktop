import mido
from abc import ABCMeta, abstractmethod

def get_input_names():
    return mido.get_input_names()

port = None
listeners = set()

def select_input( name ):
    if port:
        port.close()
        port = None
    port = mido.open_input( name, callback=notify_all )

def notify_all( msg ):
    for i in listeners:
        i.on_midi_input( msg )

class MIDIListener(metaclass=ABCMeta):
    @abstractmethod
    def on_midi_input( self, msg ):
        pass

def register( obj ):
    if isinstance( obj, MIDIListener ):
        listeners.add( obj )
    else:
        raise TypeError( "Expected MIDIListener type not {}".format( type(obj) ) )

def deregister( obj ):
    if obj in listeners:
        listeners.remove( obj )

if __name__ == '__main__':
    print( get_input_names() )
    class A(MIDIListener):
        def on_midi_input( self, msg ):
            print( msg )
    a = A()
    register( a )
    notify_all( "msg" )
    deregister(a)
    notify_all( "msg" )

import mido
from abc import ABCMeta, abstractmethod


def get_input_names():
    return mido.get_input_names()


port = None
listeners = set()


def select_input(name):
    global port
    if port:
        port.close()
        port = None
    port = mido.open_input(name, callback=notify_all)


def start():
    names = get_input_names()
    v61s = list(
        filter(lambda name: name.startswith("V61") and name.endswith("0"), names)
    )
    if len(v61s):
        select_input(v61s[0])
    else:
        select_input(names[0])


def notify_all(msg):
    global listeners
    for i in listeners:
        i.on_midi_input(msg)


class MIDIListener(metaclass=ABCMeta):
    @abstractmethod
    def on_midi_input(self, msg):
        pass


def register(obj):
    global listeners
    if isinstance(obj, MIDIListener):
        listeners.add(obj)
    else:
        raise TypeError("Expected MIDIListener type not {}".format(type(obj)))


def deregister(obj):
    global listeners
    if obj in listeners:
        listeners.remove(obj)


start()

if __name__ == "__main__":
    print(get_input_names())

    class A(MIDIListener):
        def on_midi_input(self, msg):
            print(msg)

    a = A()
    register(a)
    notify_all("msg")
    deregister(a)
    notify_all("msg")

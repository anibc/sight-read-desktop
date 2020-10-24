import mido
import sightread.midi.input as midiinput
from sightread.note.viewablenotes import ViewableNote
from sightread.note.model import NoteModel
from sightread.player import Player
from sightread import note
import random


class StaticPlayer(Player, midiinput.MIDIListener):
    def __init__(self, sl):
        self.sl = sl
        self.tracknotes = NoteModel(TwoHandWhiteRandGen())
        self.playednotes = NoteModel()
        self.curtime = 0
        midiinput.register(self)
        # midiname = next( ( n for n in mido.get_input_names() if 'V61' in n ) )
        # self.midi_input = mido.open_input( midiname, callback=self.midi_callback )

    def on_midi_input(self, msg):
        print(msg)
        if msg.type == "note_on":
            self.playednotes.insert(ViewableNote(msg.note, 0, 10))
            left = list(
                filter(lambda n: n.st == self.tracknotes.l[0].st, self.tracknotes.l)
            )
            if all(
                (
                    i in set([n.n for n in self.playednotes.l])
                    for i in set([n.n for n in left])
                )
            ):
                self.curtime += 10
                for n in left:
                    self.tracknotes.remove(n)
        elif msg.type == "note_off":
            self.playednotes.l = list(
                filter(lambda n: n.n != msg.note, self.playednotes.l)
            )
        self.sl.update()
        print("midi event picked up")


def OneHandWhiteRandGen():
    i = 0
    while True:
        i += 10
        n = random.randrange(note.SHEETLOW.n, note.SHEETHIGH.n)
        yield (ViewableNote(note.Note(n).white(), i, i + 10))


def TwoHandWhiteRandGen():
    i = 0
    while True:
        i += 10
        n = random.randrange(note.SHEETLOW.n, note.SHEETHIGH.n)
        m = random.randrange(note.SHEETLOW.n, note.SHEETHIGH.n - 1)
        if m == n:
            m += 1
        yield (
            ViewableNote(note.Note(n), i, i + 10),
            ViewableNote(note.Note(m), i, i + 10),
        )

from sightread import note
from sightread.viewablenotes import ViewableNote


"""
Random or serial note/chord generators

inputs:
    random?
    notes or chords?
    note range minimum
    note range maximum
    note from particular scale(s)
    note from particular set of notes   #not as important
    for serial generator, SCAN or CSCAN?
    serially read notes from midi
"""

# Always return list of notes


class NoteGen:
    """
    create and instance ngen using generation options
    and call ngen.next() or next(ngen) or iterate
    through object to generate set of Notes
    """

    def __init__(self):
        pass

    def __iter__(self):
        yield self.next()

    def next(self):
        return [ViewableNote(note.Note(note.MIDDLEC))]

class CustomGen(NoteGen):
    """
    source is Notes
    """
    def __init__(self, args):
        pass

    def next(self):
        pass

class PatternGen(NoteGen):
    """
    source is patterns(major, minor)
    """
    pass

class PresetGen(NoteGen):
    """
    source is File/Series(i.e. Hanon)
    """
    pass

def NoteGenFactory(args):
    GenMap = {'Notes': CustomGen, 'Pattern': PatternGen, 'Preset': PresetGen}
    return GenMap[args['source']](args)




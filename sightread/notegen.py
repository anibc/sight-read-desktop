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
    and call next(ngen) or iterate through object to
    generate set of Notes
    """

    def __init__(self):
        pass

    def __iter__(self):
        yield [ViewableNote(note.Note(note.MIDDLEC))]

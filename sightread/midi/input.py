import mido

def get_input_names():
    return mido.get_input_names()

if __name__ == '__main__':
    print( get_input_names() )

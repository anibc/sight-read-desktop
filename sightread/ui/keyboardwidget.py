from PyQt5.QtWidgets import QWidget


class KeyboardWidget(QWidget):
    def __init__(self, notes):
        super().__init__()
        self.notes = notes

from PyQt5.QtWidgets import QWidget

class VisualizerWidget(QWidget):
    def __init__(self, notes):
        super().__init__()
        self.notes = notes

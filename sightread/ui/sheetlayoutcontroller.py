class SheetLayoutController:
    def __init__( self, sl ):
        self.sl = sl
        self.notes = []
        self.mode = "static"
    @property
    def mode( self ):
        return self._mode
    @mode.setter
    def mode( self, val ):
        self._mode = StaticControllerMode() if val == "static" else DynamicControllerMode()

class StaticControllerMode():
    pass

class DynamicControllerMode():
    pass

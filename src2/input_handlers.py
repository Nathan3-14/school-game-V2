import keyboard
from .classes import Vector

class InputHandler:
    def __init__(self) -> None:
        from .classes import Player
        self._vector = Vector()
        self.player = Player

    def get_input(self) -> Vector:
        return self._vector

class KeyboardHandler(InputHandler):
    def __init__(self) -> None:
        self.key_presses = {}
        super().__init__()

    def is_just_pressed(self, key: str) -> bool:
        if (not keyboard.is_pressed(key)):
            self.key_presses[key] = False
            return False
        if key in list(self.key_presses.keys()):
            if self.key_presses[key]:
                return False
            else:
                self.key_presses[key] = True
                return True
        else:
            self.key_presses[key] = True
            return True

    def get_input(self) -> Vector:
        _vector = Vector(
            self.is_just_pressed("a")*-1 + self.is_just_pressed("d")*1,
            self.is_just_pressed("w")*-1 + self.is_just_pressed("s")*1
        )
        return _vector

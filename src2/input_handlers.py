from typing import Dict, List
from .classes import Vector

class InputHandler:
    def __init__(self) -> None:
        from .classes import Player
        self._vector = Vector()
        self.player: Player | None = None

    def get_input(self) -> Vector:
        return self._vector

class TypingHandler(InputHandler):
    def get_input(self) -> Vector:
        match input("Enter move").lower():
            case "a":
                return Vector(-1, 0)
            case "d":
                return Vector(1, 0)
            case "w":
                return Vector(0, -1)
            case "s":
                return Vector(0, 1)
            case "q" | "quit" | "exit":
                quit()
            case _:
                return self.get_input()

class KeyboardHandler(InputHandler):
    def __init__(self) -> None:
        super().__init__()
        self.key_presses: Dict[str, bool] = {}

    def is_just_pressed(self, key: str) -> bool:
        import keyboard
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
        if self.is_just_pressed("q"):
            quit()
        return _vector

class TestHandler(InputHandler):
    def __init__(self, input_list: List[str]) -> None:
        super().__init__()
        self.input_list = input_list
        self.input_index = -1
    
    def get_input(self) -> Vector:
        self.input_index += 1
        if self.input_index >= len(self.input_list):
            quit()

        match self.input_list[self.input_index]:
            case "w":
                return Vector(0, -1)
            case "s":
                return Vector(0, 1)
            case "a":
                return Vector(-1, 0)
            case "d":
                return Vector(1, 0)
        return Vector(0, 0)


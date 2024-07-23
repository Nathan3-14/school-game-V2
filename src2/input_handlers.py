from .classes import Pos, Vector

class InputHandler:
    def __init__(self) -> None:
        pass

    def get_input(self) -> Vector:
        return Vector(0, 0)
        

class InputKeywordHandler(InputHandler):
    def __init__(self) -> None:
        super().__init__()
    
    def get_input(self) -> Vector:
        _input = input("Enter your keypresses (wasd)\n>> ")
        _vector = Vector()
        _vector += Vector(1*_input.count("d") + -1*_input.count("a"), 1*_input.count("s")+-1*_input.count("w"))

        return _vector


import keyboard
from .classes import Vector

class InputHandler:
    def __init__(self) -> None:
        self._vector = Vector()
        self.player = None

    def get_input(self) -> Vector:
        return self._vector
    
    def left(self):
        self._vector.x -= 1
        self.player.world.frame()
    def right(self):
        self._vector.x += 1
        self.player.world.frame()
    def up(self):
        self._vector.y -= 1
        self.player.world.frame()
    def down(self):
        self._vector.y += 1
        self.player.world.frame()
        

# class InputKeywordHandler(InputHandler):
#     def __init__(self) -> None:
#         super().__init__()
    
#     def get_input(self) -> Vector:
#         _input = input("Enter your keypresses (wasd)\n>> ")
#         _vector = Vector()
#         _vector += Vector(1*_input.count("d") + -1*_input.count("a"), 1*_input.count("s")+-1*_input.count("w"))

#         return _vector

class KeyboardHandler(InputHandler):
    def __init__(self) -> None:
        super().__init__()
        keyboard.on_press(lambda key: self.move(key.name))
        # keyboard.on_press_key("a", self.left)
        # keyboard.on_press_key("d", self.right)
        # keyboard.on_press_key("w", self.up)
        # keyboard.on_press_key("s", self.down)
    
    def move(self, key: str) -> None:
        print(f"read key {key}")
        match key:
            case "a":
                self.left()
            case "d":
                self.down()
            case "w":
                self.up()
            case "d":
                self.down()

    # def get_input(self) -> Vector:
    #     # _vector = Vector(
    #     #     self.is_just_pressed("a")*-1 + self.is_just_pressed("d")*1,
    #     # 0)
    #         # self.up_pressed*-1 + self.down_pressed*1)
    #     return _vector


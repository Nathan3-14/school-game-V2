import time
from typing import List

class Pos:
    def __init__(self, x: int=0, y: int=0) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, other: "Pos"):
        return Pos(
            self.x + other.x,
            self.y + other.y
        )

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

class Vector(Pos):
    def __init__(self, x: int=0, y: int=0) -> None:
        super().__init__(x, y)
    
    def __eq__(self, other: object):
        if isinstance(other, Vector):
            return (self.x == other.x) and (self.y == other.y)
        return NotImplemented

    def __ne__(self, other: object):
        return not self.__eq__(other)


directions = {
    ">": Vector(1, 0),
    "<": Vector(-1, 0),
    "^": Vector(0, 1),
    "v": Vector(0, -1)
}
directions_keys = list(directions.keys())


class Door:
    def __init__(self, start_room_pos: Pos, direction: str) -> None:
        self.door_position = start_room_pos
        self.door_direction = direction


class Player:
    from .input_handlers import InputHandler

    def __init__(self, input_handler: InputHandler):
        self.position = Pos(0, 0) #? Start position from P in section
        self.world = World
        self.handler = input_handler
        self.handler.player = self
    
    def get_input(self) -> None:
        _input_vector = Vector()
        have_input = False
        
        while _input_vector == Vector():
            # print("getting input")
            _input_vector = self.handler.get_input()
            # print(f"{_input_vector} == {Vector()}: {_input_vector==Vector()}")
            # print(f"{_input_vector} != {Vector()}: {_input_vector!=Vector()}")
            # time.sleep(1)
        self.move(_input_vector)

    def move(self, vector: Vector) -> None:
        self.position += vector



class Section:
    def __init__(self, area: List[str], start: Pos, end: Pos, is_discovered: bool=False, is_start: bool=False) -> None:
        self.display_area = area
        self.doors = []

        self.player_start_position = None
        for index, line in enumerate(area):
            if "P" not in line:
                continue
            self.player_start_position = Pos(line.index("P"), index)
        self.is_discovered = is_discovered

        self.start = start
        self.end = end

        display_area_reversed = self.display_area.copy()
        display_area_reversed.reverse()
        for index, line in enumerate(display_area_reversed):
            if not any(value in line for value in directions_keys):
                continue

            for char_index, char in enumerate(line):
                if char not in directions_keys:
                    continue
                self.doors.append(
                    Door(
                        Pos(char_index, index),
                        directions[char] # type: ignore
                    )
                )



class World:
    def __init__(self, world: List[Section], start_section: Section, player: Player) -> None:
        self.sections = {
            section: section.is_discovered for section in world
            # section: True for section in world #? Test Line
        }
        self.start_section = start_section
        self.player = player
        self.player.position = self.start_section.player_start_position # type: ignore
        self.player.world = self # type: ignore
        
        self.display_old: List[str] = []

        self.collisions = ["#", "~"]
    
    def display(self) -> List:
        display = ["                    "] * 10

        for section, is_in_view in self.sections.items():
            if not is_in_view:
                continue
            
            for line_index, line in enumerate(section.display_area):
                #? iterate and replace with different line each time from display
                replace_string = [char for char in display[section.start.y+line_index]]

                line_replaced = ""
                for char_index, char in enumerate(line):
                    if char == " ":
                        replace_char = display[section.start.y+line_index][section.start.x+char_index]
                    else:
                        replace_char = char
                    line_replaced += replace_char
                
                replace_string[section.start.x:section.end.x] = line_replaced
                display[section.start.y+line_index] = "".join(replace_string).replace("P", ".")

        display[self.player.position.y] = "".join(
            [
                char if index != self.player.position.x else "@" for index, char in enumerate(display[self.player.position.y])
            ]
        )

        return display
        

    def frame(self) -> None:
        self.player.get_input()
        print("player input recieved")
        
        print("\n".join(self.display()))

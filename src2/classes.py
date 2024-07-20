import enum
from typing import List


class Pos:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, other: "Pos"):
        return Pos(
            self.x + other.x,
            self.y + other.y
        )

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


directions = {
    ">": Pos(1, 0),
    "<": Pos(-1, 0),
    "^": Pos(0, 1),
    "v": Pos(0, -1)
}
directions_keys = list(directions.keys())


class Door:
    def __init__(self, start_room_pos: Pos, direction: str) -> None:
        self.door_position = start_room_pos
        self.door_direction = direction


class Section:
    def __init__(self, area: List[str], start: Pos, end: Pos) -> None:
        self.display_area = area
        self.doors = []

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
                        directions[char]
                    )
                )



class World:
    def __init__(self, world: List[Section]) -> None:
        self.sections = {
            # section: is_discovered for section in world
            # section: False for section in world
            section: True for section in world #? Test Line
        }
    
    def display(self) -> None:
        display = ["                    "] * 10

        for section, is_in_view in self.sections.items():
            if not is_in_view:
                continue

            [char for char in display][section.start.x:section.end.x] = section #? iterate and replace with different line each time from display
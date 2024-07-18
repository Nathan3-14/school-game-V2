from typing import List, Tuple


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


class Player:
    def __init__(self) -> None:
        self.pos = Pos(0, 0)
        self.current_room_name = ""
    
    def move(self, vector: Pos):
        self.pos += vector


class Door:
    def __init__(self, room_name: str, room_pos: Pos) -> None:
        self.link_room = room_name
        self.link_room_position = room_pos


class Room:
    def __init__(self, name: str, map: List[str]) -> None:
        self.name = name
        self.map = map
        self.doors = {}


class World:
    def __init__(self, room_list: List[Room], start_room_name: str, player: "Player") -> None:
        self.rooms = {
            room.name: room for room in room_list
        }
        self.player = player
        self.player.current_room_name = start_room_name
    
    def display(self):
        current_room = self.rooms[self.player.current_room_name]
        for line in current_room.map:
            print(line)
        



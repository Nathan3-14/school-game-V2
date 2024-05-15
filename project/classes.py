from typing import List, Tuple, Dict
from rich.console import Console
from .funcs import error


class pos:
    def __init__(self,
             start_x: int | str = 0,
             start_y: int | str = 0,
        ):
        try:
            self.x = int(start_x) if isinstance(start_x, str) else start_x
            self.y = int(start_y) if isinstance(start_y, str) else start_y
        except ValueError:
            error(f"Invalid position type {start_x} or {start_y} is not a valid int", Console(), message_start="Code Err")
            self.x = 0
            self.y = 0

    def __str__(self):
        return f"<x:{self.x} y:{self.y}>"

    def __repr__(self):
        return str(self)


class Player:
    def __init__(self):
        self.icon: str = "[dodger_blue3]@[/dodger_blue3]"
        self.current_room: str = ""
        self.position: pos = pos()
    
    def update(self, vector: Tuple[int, int]):
        """
        Updates the players state according to the provided vector and world.
        """
        pass

class Room:
    def __init__(self, name: str, map: List[str], doors: Dict[Tuple[int, int], List[str]], is_start: bool):
        self.name = name
        self.map = map
        self.doors = doors
        self.is_start = is_start
        self.console = Console()
        self.start_pos = pos()

        if self.is_start:
            for index, line in enumerate(self.map):
                if "P" in line:
                    self.start_pos.y = index
                    self.start_pos.x = line.index("P")


    def show_map(self, player: "Player") -> None:
        for line_index, line in enumerate(self.map):
            line_print = f"{line}"

            for index, char in enumerate(line):
                if char != "D":
                    continue
                door_char = ""
                if index == 0:
                    door_char = "<"
                elif 0 < index < len(line)-1:
                    if line_index == 0:
                        door_char = "^"
                    elif line_index == len(self.map)-1:
                        door_char = "v"
                elif index == len(line)-1:
                    door_char = ">"
                line_print = line_print.replace("D", f"[bold chartreuse4]{door_char}[/bold chartreuse4]", 1)
            
            line_print = line_print.replace("W", "[red]#[/red]")
            line_print = line_print.replace("C", "[bright_cyan]*[/bright_cyan]")
            line_print = line_print.replace(".", " ")
            line_print = line_print.replace("~", "[orchid1]~[/orchid1]")
            line_print = line_print.replace("P", " ")

            if line_index == player.position.y:
                new_line = ""
                for index, char in enumerate(line_print):
                    if index == player.position.x:
                        player.icon
                    else:
                        new_line += char
                line_print = new_line #! FIX
        
            self.console.print(line_print)
    
    def __str__(self, is_cool: bool) -> str:
        return f"{self.name}"
    
class World:
    def __init__(self, rooms: List[Room]):
        self.rooms = {room.name: room for room in rooms}
        for room_name, room in self.rooms.items():
            if room.is_start:
                self.starting_room = room_name
        self.player = Player()
        self.player.current_room = self.starting_room
        self.player.position = self.rooms[self.starting_room].start_pos

    def display(self, room_name: str) -> None:
        self.rooms[room_name].show_map(self.player)
        
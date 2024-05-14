from typing import List, Tuple, Dict
from rich.console import Console


class Player:
    def __init__(self):
        self.icon = "[dodger_blue3]@[/dodger_blue3]"
    
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

    def show_map(self) -> None:
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
        self.player.position = self.rooms[self.starting_room]

    def display(self, room_name: str) -> None:
        self.rooms[room_name].show_map()
        
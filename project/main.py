from typing import ParamSpecKwargs
from rich.console import Console
from rich.prompt import Prompt
import yaml
import json
from .classes import Room, World


class Game:
    def __init__(self, do_clear: bool=False) -> None:
        self.console = Console()
        world_dict = yaml.load(open("world1.yml", "r"), yaml.BaseLoader)
    
        rooms = []
        for room_name, room_data in world_dict.items():
            room_map = room_data["map"]
            room_doors = room_data["doors"]
            room_temp = Room(room_name, room_data["map"], room_data["doors"], False if "start" not in list(room_data.keys()) else room_data["start"])
    
            rooms.append(room_temp)
        
        # console.print_json(json.dumps(rooms, indent=4))
        self.world = World(rooms)
        self.clear = do_clear
    
    def game_loop(self) -> None:
        self.current_room = self.world.starting_room
        while True:
            self.game_frame()
            if input() == "exit":
                quit()


    def game_frame(self) -> None:
        if self.clear:
            self.console.clear()

        current_room_data = self.world.rooms[self.current_room]
        
        self.world.display(self.current_room)
    

def main():
    game = Game()
    
    game.clear = Prompt.ask("Clear screen", choices=["y", "n"], default="y", console=game.console) == "y"
    
    game.game_loop()

import json
from random import randint
from typing import Dict, Tuple

from rich import print_json


class Pos:
    def __init__(self, x: int=0, y: int=0) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, other: "Pos") -> "Pos":
        return Pos(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: "Pos") -> "Pos":
        return Pos(
            self.x - other.x,
            self.y - other.y
        )

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other: object) -> bool:
        return (self.x == other.x) and (self.y == other.y) #type:ignore
    
    def __hash__(self):
        return hash((self.x, self.y))

class Vector(Pos):
    def __init__(self, x: int=0, y: int=0) -> None:
        super().__init__(x, y)
    
    def __eq__(self, other: object):
        if isinstance(other, Vector):
            return (self.x == other.x) and (self.y == other.y)
        return NotImplemented

    def __ne__(self, other: object):
        return not self.__eq__(other)
    
class LootTable:
    def __init__(self, table: Dict[str, Dict[str, int|Dict[str,int]]]) -> None:
        self.possible_items = {
            name: {
                "range": (data["min"], data["max"]), #type:ignore
                "weight": data["weight"] #type:ignore
            } for name, data in table["items"].items()
        }
        self.roll_counts = table["rolls"]
    
    def get_item(self) -> Tuple[str, int]:
        options = []
        for item, item_data in self.possible_items.items():
            for _ in range(item_data["weight"]): #type:ignore
                options.append(item)
        
        chosen_item_name = options[randint(0, len(options)-1)]
        chosen_item_range = self.possible_items[chosen_item_name]["range"]
        chosen_item_count = randint(chosen_item_range[0], chosen_item_range[1]) #type:ignore
        return (chosen_item_name, chosen_item_count)

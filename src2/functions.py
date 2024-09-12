import json

from .classes import Player, Section, World, Pos
from .common_classes import LootTable
from .input_handlers import InputHandler

def create_world_from_file(file_path: str, handler: InputHandler) -> World:
    data = json.load(open(file_path))

    sections = [
        Section(
            map_object["map"],
            Pos(map_object["tl_bound"][0], map_object["tl_bound"][1]),
            Pos(map_object["br_bound"][0], map_object["br_bound"][1]),
            loot_tables=map_object["loot_tables"] if "loot_tables" in list(map_object.keys()) else {}
        ) for map_object in data["sections"]
    ]
    print(data["loot"])
    loot_tables = {
        loot_table_name: LootTable(loot_table_data) for loot_table_name, loot_table_data in data["loot"].items()
    }

    return World(
        sections,
        sections[0],
        Player(handler),
        loot_tables=loot_tables
    )

def set_in_string(old_string: str, index: int, replace_char: str) -> str:
    new_string = ""
    for current_index, char in enumerate(old_string):
        if current_index == index:
            new_string += replace_char
        else:
            new_string += char
    return new_string

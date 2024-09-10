import json

from .classes import Player, World
from .input_handlers import InputHandler

def create_world_from_file(file_path: str, handler: InputHandler) -> World:
    data = json.load(open(file_path))

    sections = []
    loot_table = data["loot"]["chest1"]

    return World(
        sections,
        sections[0],
        player=Player(handler),
        chest_table=loot_table
    )

def set_in_string(old_string: str, index: int, replace_char: str) -> str:
    new_string = ""
    for current_index, char in enumerate(old_string):
        if current_index == index:
            new_string += replace_char
        else:
            new_string += char
    return new_string

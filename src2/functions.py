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
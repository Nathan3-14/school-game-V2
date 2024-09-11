import time
from typing import Dict, List
from .common_classes import LootTable, Vector, Pos


directions = {
    ">": Vector(1, 0),
    "<": Vector(-1, 0),
    "^": Vector(0, 1),
    "v": Vector(0, -1)
}
directions_keys = list(directions.keys())


# class Door:
#     def __init__(self, start_room_pos: Pos, direction: Vector) -> None:
#         self.door_position = start_room_pos
#         self.door_direction = direction


class Player:
    from .input_handlers import InputHandler

    def __init__(self, input_handler: InputHandler):
        self.position = Pos(0, 0) #? Start position from P in section
        self.inventory: Dict[str, int] = {}
        self.world = World
        self.last_move = Vector()
        self.handler = input_handler
        self.handler.player = self #type:ignore #! complains about player attribute no on player !#
    
    def get_input(self) -> None:
        _input_vector = Vector()
        
        while _input_vector == Vector():
            _input_vector = self.handler.get_input()
        self.move(_input_vector)

    def move(self, vector: Vector) -> None:
        self.position += vector
        self.last_move = vector
    
    def move_back(self) -> None:
        self.position -= self.last_move
    
    def add_item_to_inventory(self, item_name: str, count: int) -> None:
        if item_name in list(self.inventory.keys()):
            self.inventory[item_name] += count
        else:
            self.inventory[item_name] = count

    def add_item_to_inventory_with_text(self, item_name: str, count: int) -> bool:
        self.add_item_to_inventory(item_name, count)
        self.world.message = (f"You got {count} {item_name}{'s' if count > 1 else ''}")
        return True
    
    def use_item_from_inventory(self, item_name: str, count: int=1) -> bool:
        if item_name in self.inventory:
            if self.inventory[item_name] >= count:
                self.inventory[item_name] -= count
                return True
            else:
                return False
        else:
            return False
    
    def use_item_from_inventory_with_text(self, item_name: str, count: int=1) -> bool:
        if self.use_item_from_inventory(item_name, count=count):
            self.world.message = (f"You used <{count}> {item_name}{'s' if count > 1 else ''}")
            return True
        else:
            self.world.message = (f"You need <{count}> {item_name}{'s' if count > 1 else ''}>")
            return False


class Section:
    def __init__(self, area: List[str], start: Pos, end: Pos, loot_tables: Dict[Pos, LootTable]={}, is_discovered: bool=False) -> None:
        self.display_area = area
        self.start = start
        self.end = end

        self.player_start_position = None
        for index, line in enumerate(area):
            if "P" not in line:
                continue
            self.player_start_position = Pos(line.index("P"), index)
            self.set(self.player_start_position, " ")
        self.is_discovered = is_discovered

        self.loot_tables = loot_tables


        display_area_reversed = self.display_area.copy()
        display_area_reversed.reverse()
    
    def set(self, position: Pos, target_character: str, offset: bool=False) -> None:
        from .functions import set_in_string

        position_offset = position - self.start #? Needed in order to account for position being relative to map not to section
        self.display_area[position_offset.y] = set_in_string(self.display_area[position_offset.y], position_offset.x, target_character)
    

    def __contains__(self, player_object: Player):
        positions = [
            Pos(x, y)
            for x in range(self.start.x, self.end.x+2)
            for y in range(self.start.y, self.end.y+2)
        ]

        return player_object.position in positions



class World:
    def __init__(self, world: List[Section], start_section: Section, player: Player, loot_tables: Dict[str, LootTable]={}) -> None:
        self.sections = [
            section for section in world
            # section: True for section in world #? Test Line
        ]
        self.start_section = start_section
        self.start_section.is_discovered = True
        self.player = player
        self.player.position = self.start_section.player_start_position # type: ignore
        self.player.world = self # type: ignore

        self.display: List[str] = []
        self.message = ""
        
        self.collisions = ["#"]

        self.loot_tables = loot_tables


        self.render() #? Renders the first screen of the game
    
    def update_display(self, skip_actions: bool=False) -> None:
        display = ["                    "] * 10

        for section in self.sections:
            if not section.is_discovered:
                continue
            
            for line_index, line in enumerate(section.display_area):
                #? iterate and replace with different line each time from display
                replace_string = [char for char in display[section.start.y+line_index]]

                line_replaced = ""
                for char_index, char in enumerate(line): #? For layering the sections correctly
                    if char == ",":
                        replace_char = display[section.start.y+line_index][section.start.x+char_index]
                    else:
                        replace_char = char
                    line_replaced += replace_char
                
                replace_string[section.start.x:section.end.x] = line_replaced
                display[section.start.y+line_index] = "".join(replace_string).replace("P", " ")
                display[section.start.y+line_index] = "".join(replace_string).replace(".", " ")

        if self.check_collisions():
            self.player.move_back()
        if not skip_actions:
            self.check_actions()


        display[self.player.position.y] = "".join(
            [
                char if index != self.player.position.x else "@" for index, char in enumerate(display[self.player.position.y])
            ]
        ) #? For placing the player at the correct position

        self.display = display
    
    def check_collisions(self) -> bool:
        try:
            return self.display[self.player.position.y][self.player.position.x] in self.collisions
        except IndexError: #? Used to fix error on first rendering of game screen
            return False
    
    def check_actions(self) -> None:
        try:
            self.display[self.player.position.y]
        except IndexError:#? Used to fix error on first rendering of game screen
            return None
        
        current_icon = self.display[self.player.position.y][self.player.position.x]
        match current_icon:
            case ">" | "<" | "^" | "v":
                match current_icon:
                    case ">":
                        self.player.move(Vector(1, 0))
                    case "<":
                        self.player.move(Vector(-2, 0))
                    case "v":
                        self.player.move(Vector(0, 1))
                    case "^":
                        self.player.move(Vector(0, -1))
                for section in self.sections:
                    if self.player in section:
                        section.is_discovered = True
                self.update_display(skip_actions=True)
            case "=":
                if self.player.use_item_from_inventory_with_text("key", 1):
                    self.get_current_section().set(self.player.position, ".")
                else:
                    self.player.move_back()
            case "*":
                loot_table_name = self.get_current_section().loot_tables[self.player.position-self.get_current_section().start]
                loot_table = self.loot_tables[loot_table_name]
                item_gotten = loot_table.get_item()
                self.player.add_item_to_inventory_with_text(item_gotten[0], item_gotten[1])
            case "+":
                self.player.add_item_to_inventory_with_text("key", 1)
            case "~":
                print("You Win!")
                quit()
            case _:
                pass
    
    def get_current_section(self) -> Section | None:
        for section in self.sections:
            if self.player in section:
                return section
        return None

    def render(self, skip_print: bool=False):
        self.update_display()
        if not skip_print:
            print(f"{self.message}")
            self.message = ""
            print(f"Inventory: {','.join([f'{item} ({count})' for item, count in self.player.inventory.items() if count >= 1])}")
            print("\n".join(self.display))

    def frame(self) -> None:
        self.player.get_input()
        self.render(skip_print=True)
        self.render()

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


class Section:
    def __init__(self, area: List[str], start: Pos, end: Pos, is_discovered: bool=False) -> None:
        self.display_area = area

        self.player_start_position = None
        for index, line in enumerate(area):
            if "P" not in line:
                continue
            self.player_start_position = Pos(line.index("P"), index)
        self.is_discovered = is_discovered

        self.start = start
        self.end = end

        display_area_reversed = self.display_area.copy()
        display_area_reversed.reverse()
    

    def __contains__(self, player_object: Player):
        positions = [
            Pos(x, y)
            for x in range(self.start.x, self.end.x+2)
            for y in range(self.start.y, self.end.y+2)
        ]

        return player_object.position in positions



class World:
    def __init__(self, world: List[Section], start_section: Section, player: Player, chest_table: LootTable | None=None) -> None:
        self.sections = [
            section for section in world
            # section: True for section in world #? Test Line
        ]
        self.start_section = start_section
        self.player = player
        self.player.position = self.start_section.player_start_position # type: ignore
        self.player.world = self # type: ignore

        self.display: List[str] = []
        
        self.collisions = ["#"]

        self.chest_table = chest_table


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
                    if char == " ":
                        replace_char = display[section.start.y+line_index][section.start.x+char_index]
                    else:
                        replace_char = char
                    line_replaced += replace_char
                
                replace_string[section.start.x:section.end.x] = line_replaced
                display[section.start.y+line_index] = "".join(replace_string).replace("P", ".")

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
                if "key" not in list(self.player.inventory.keys()):
                    self.player.move_back()
                elif self.player.inventory["key"] >= 1:
                    self.player.inventory["key"] -= 1
                else:
                    self.player.move_back()
            case "*":
                self.chest_table.get_item() #type:ignore
            case _:
                pass
    
    def render(self, skip_print: bool=False):
        self.update_display()
        if not skip_print:
            print("\n".join(self.display))

    def frame(self) -> None:
        self.player.get_input()
        self.render(skip_print=True)
        self.render()

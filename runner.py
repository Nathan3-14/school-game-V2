import src


rooms = [
    src.Room(
        "Hall",
        [
            "#######",
            "<  #  >",
            "##  #*#",
            "###v###"
        ]
    ),
    src.Room(
        "Dining Room",
        [
            "##∧##"
            "#  *#"
            "#####"
        ]
    ),
    src.Room(
        "Living Room"
    )
]

player = src.Player()
world = src.World(rooms, "Hall", player)

world.display()

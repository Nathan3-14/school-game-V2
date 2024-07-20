import src


rooms = [
    src.Room(
        "start",
        [
            "#######",
            "#& #  >",
            "##  #*#",
            "###v###"
        ],
        [
            src.Door("room_2", src.Pos(3, 0), src.Pos(2, 2)),
            src.Door("room_3", src.Pos(6, 2), src.Pos(0, 1))
        ]
    ),
    src.Room(
        "room_2",
        [
            "##∧##"
            "#  *#"
            "#####"
        ],
        [
            src.Door("start", src.Pos(2, 2), src.Pos(3, 0))
        ]
    ),
    src.Room(
        "room_3",
        [
            "#######",
            "#     >",
            "# ## ##",
            "< #   #",
            "#######"
        ],
        [
            src.Door("start", src.Pos(0, 1), src.Pos(6, 2)),
            src.Door("room_4", src.Pos(6, 3), src.Pos(0, 1))
        ]
    ),
    src.Room(
        "room_4",
        [
            "#######"
            "# #  =#",
            "<   #~#",
            "#######"
        ],
        [
            src.Door("room_3", src.Pos(0, 1), src.Pos(6, 3))
        ]
    )
]

player = src.Player()
world = src.World(rooms, "start", player)

world.display()

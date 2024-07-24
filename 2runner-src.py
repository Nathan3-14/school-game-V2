import src2
import time


sections = [
    src2.Section(
        [
            "#####",
            "#P..#",
            "#...>",
            "#####"
        ],
        src2.Pos(0, 0),
        src2.Pos(4, 3),
        is_discovered=True
    ),
    src2.Section(
        [
            " #######",
            " <.....#",
            "####...#",
            "#......>",
            "##...###",
            " #####  "
        ],
        src2.Pos(4, 1),
        src2.Pos(11, 6)
    ),
    src2.Section(
        [
            "#^###",
            "<...#",
            "###v#"
        ],
        src2.Pos(12, 3),
        src2.Pos(16, 5)
    ),
    src2.Section(
        [
            "#####^#",
            "#~.=..#",
            "#######"
        ],
        src2.Pos(10, 6),
        src2.Pos(16, 8)
    ),
    src2.Section(
        [
            "###",
            "#*#",
            "#v#"
        ],
        src2.Pos(12, 0),
        src2.Pos(14, 2)
    )
]

player = src2.Player(src2.KeyboardHandler())

world = src2.World(
    sections,
    sections[0],
    player
)
while True:
    world.frame()


# world.display()
# time.sleep(1)
# player.move(src2.Pos(1, 0))
# world.display()
# time.sleep(1)
# player.move(src2.Pos(1, 0))
# world.display()
# time.sleep(1)
# player.move(src2.Pos(0, 1))
# world.display()
# time.sleep(1)


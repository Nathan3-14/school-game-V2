import src2
import time
import sys


chest1_table = src2.LootTable({
    "key": {
        "min": 1,
        "max": 2,
        "weight": 1
    },
    "gold": {
        "min": 3,
        "max": 5,
        "weight": 1
    }
})


sections = [
    src2.Section(
        [
            "#####",
            "#P..#",
            "#...>",
            "#####"
        ],
        src2.Pos(0, 0),
        src2.Pos(4, 3)
    ),
    src2.Section(
        [
            ",#######",
            ",<.....#",
            "####...#",
            "#......>",
            "##...###",
            ",##v##,,"
        ],
        src2.Pos(4, 1),
        src2.Pos(11, 6)
    ),
    src2.Section(
        [
            "##^##",
            "#..+#",
            "#####"
        ],
        src2.Pos(5, 7),
        src2.Pos(10, 8)
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
        src2.Pos(14, 2),
        loot_tables={
            src2.Pos(1, 1): "chest1"
        }
    )
]

if "-t" in sys.argv:
    player = src2.Player(src2.TypingHandler())
else:
    player = src2.Player(src2.KeyboardHandler())


world = src2.World(
    sections,
    sections[0],
    player,
    {
        "chest1": chest1_table
    }
)

while True:
    world.frame()


import src2


world = src2.World([
    src2.Section([
        "#####",
        "#...#",
        "#...>",
        "#####"
    ],
    src2.Pos(0, 0)
    )
])

world.display()

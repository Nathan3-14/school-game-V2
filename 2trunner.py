import src2

sections = [
    src2.Section(
        [
            "#####",
            "# P #",
            "#   #",
            "#####"
        ],
        src2.Pos(0, 0),
        src2.Pos(4, 4)
    )
]
player = src2.Player(src2.TestHandler([
]))
world = src2.World(
    sections,
    sections[0],
    player
)

while True:
    world.frame()
    world.sections[0].set(src2.Pos(0, 0), "!")
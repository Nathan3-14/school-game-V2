from src2 import create_world_from_file, TypingHandler


world = create_world_from_file("./school_world.json", TypingHandler())
while True:
    world.frame()

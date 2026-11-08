clear()

while True:
    for _ in range(get_world_size()):
        for _ in range(get_world_size()):
            dig()
        move(North)
    move(East)
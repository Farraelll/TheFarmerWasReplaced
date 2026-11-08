clear()

def silvicultura():
    if can_harvest():
        harvest()
        if (get_pos_x() + get_pos_y()) % 2 == 0:
            plant(Entities.Tree)
        else:
            plant(Entities.Bush)


def main():
    while True:
        for _ in range(get_world_size()):
            for _ in range(get_world_size()):
                silvicultura()
                move(North)
            move(East)

if __name__ == "__main__":
    main()
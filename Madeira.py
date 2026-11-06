clear()

while True:
    for _ in range(get_world_size()):
        for _ in range(get_world_size()):
            if can_harvest():
                harvest()
            if (get_pos_x() + get_pos_y()) % 2 == 0:
                plant(Entities.Tree)
                if get_water() < 0.3:
                    use_item(Items.Water)
            else:
                plant(Entities.Bush)
            move(North)
        move(East)

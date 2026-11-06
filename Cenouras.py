from utils import preparar

preparar(Entities.Carrot)

while True:
    for _ in range(get_world_size()):
        for _ in range(get_world_size()):
            if can_harvest():
                harvest()
            plant(Entities.Carrot)
            if get_water() < 0.25:
                use_item(Items.Water)
            move(North)
        move(East)
    
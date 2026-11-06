from utils import preparar

preparar(Entities.Carrot)

while True:
    for _ in range(get_world_size()):
        for _ in range(get_world_size()):
            if can_harvest():
                harvest()
            plant(Entities.Carrot)
            move(North)
        move(East)
    
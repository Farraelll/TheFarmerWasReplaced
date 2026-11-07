from utils import preparar, semear, tamanho

preparar()
semear(Entities.Carrot)

while True:
    for _ in range(tamanho):
        for _ in range(tamanho):
            if can_harvest():
                harvest()
            plant(Entities.Carrot)
            if get_water() < 0.25:
                use_item(Items.Water)
            move(North)
        move(East)
    
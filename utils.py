def irPara(x, y):
    tamanho = get_world_size()
    metade = tamanho // 2

    distancia = (x - get_pos_x() + metade) % tamanho - metade
    direcao = (West, East)[distancia > 0]
    for _ in range(abs(distancia)):
        move(direcao)

    distancia = (y - get_pos_y() + metade) % tamanho - metade
    direcao = (South, North)[distancia > 0]
    for _ in range(abs(distancia)):
        move(direcao)

def preparar(semente):
    clear()
    tamanho = get_world_size()
    
    for _ in range(tamanho):
        for _ in range(tamanho):
            if get_ground_type() == Grounds.Grassland :
                till()
            plant(semente)
            use_item(Items.Water)
            move(North)
        move(East)
tamanho = get_world_size()

def ir_para(x, y):
    'Usa as coordenadas (x, y) para ir até a posição desejada'
    
    metade = tamanho // 2
    distancia = (x - get_pos_x() + metade) % tamanho - metade
    direcao = (West, East)[distancia > 0]
    for _ in range(abs(distancia)):
        move(direcao)

    distancia = (y - get_pos_y() + metade) % tamanho - metade
    direcao = (South, North)[distancia > 0]
    for _ in range(abs(distancia)):
        move(direcao)

def preparar():
    'Ara o terreno e volta para a posição inicial (0, 0)'
    
    for _ in range(tamanho):
        for _ in range(tamanho):
            if get_ground_type() == Grounds.Grassland :
                till()
            if can_harvest():
                harvest()
            move(North)
        move(East)

def semear(semente, quantidade=1):
    'Planta e rega a semente em todo o terreno.'

    for _ in range(tamanho):
        for _ in range(tamanho):
            plant(semente)
            quantidade = 4 - get_water() * 4
            if quantidade >= 1:
                use_item(Items.Water, quantidade)
            move(North)
        move(East)
    
if __name__ == "__main__":
    ir_para(0, 0)
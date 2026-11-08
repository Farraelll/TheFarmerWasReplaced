from utils import *

preparar()

def encontrar_mortas():
    mortas = []
    for _ in range(tamanho):
        for _ in range(tamanho):
            if get_entity_type() == Entities.Dead_Pumpkin:
                plant(Entities.Pumpkin)
                mortas.append((get_pos_x(), get_pos_y()))
            move(North)
        move(East)
    return mortas


def replantar_mortas(mortas):
    while mortas:
        for x, y in mortas[:]:
            ir_para(x, y)
            if get_entity_type() == Entities.Dead_Pumpkin:
                plant(Entities.Pumpkin)
            else:
                mortas.remove((x, y))

def main():
    while True:
        semear(Entities.Pumpkin)
        mortas = encontrar_mortas()
        replantar_mortas(mortas)

        while not can_harvest():
            if get_entity_type() == Entities.Dead_Pumpkin:
                plant(Entities.Pumpkin)
            do_a_flip()
        harvest()

if __name__ == "__main__":
    main()
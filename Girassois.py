from utils import *

def colher(posicoes):
    for x, y in posicoes:
        ir_para(x, y)
        while not can_harvest():
            pass
        harvest()

def plantar_e_medir(lista):
    for _ in range(tamanho):
        for _ in range(tamanho):
            plant(Entities.Sunflower)
            if get_water() < 0.5:
                use_item(Items.Water)
            petalas = measure()
            if petalas < 10:
                lista["poucas"].append((get_pos_x(), get_pos_y()))
            else:
                lista[petalas].append((get_pos_x(), get_pos_y()))
            move(North)
        move(East)

def main():
    preparar()
    while True:
        dictPetalas = {
            15: [],
            14: [],
            13: [],
            12: [],
            11: [],
            10: [],
            "poucas": []
        }
        plantar_e_medir(dictPetalas)
        for girassois in dictPetalas:
            colher(dictPetalas[girassois])

if __name__ == "__main__":
    main()
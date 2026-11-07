from utils import *

def colher(posicoes):
    for x, y in posicoes:
        ir_para(x, y)
        if can_harvest():
            harvest()

def plantar_e_medir(lista):
    for _ in range(tamanho):
        for _ in range(tamanho):
            plant(Entities.Sunflower)
            petalas = measure()
            if petalas < 10:
                lista["poucas"].append((get_pos_x(), get_pos_y()))
            else:
                lista[petalas].append((get_pos_x(), get_pos_y()))


while True:
    preparar()
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
    for grandes in dictPetalas:
        colher(dictPetalas[grandes])
    
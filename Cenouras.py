from utils import preparar, semear, tamanho

preparar()
semear(Entities.Carrot)

def plantar_cenouras():
    if can_harvest():
        harvest()
    plant(Entities.Carrot)

def main():
    while True:
        for _ in range(tamanho):
            for _ in range(tamanho):
                plantar_cenouras()
                move(North)
            move(East)

if __name__ == "__main__":
    main()
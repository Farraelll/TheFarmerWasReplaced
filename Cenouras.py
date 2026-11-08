from utils import preparar, semear, tamanho

preparar()
semear(Entities.Carrot)

def main():
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

if __name__ == "__main__":
    main()
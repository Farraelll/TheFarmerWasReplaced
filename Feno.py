clear()

tamanho = get_world_size()

def main():
    while True:
        for _ in range(tamanho):
            for _ in range(tamanho):
                if can_harvest():
                    harvest()
                move(North)
            move(East)

if __name__ == "__main__":
    main()
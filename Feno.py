clear()

tamanho = get_world_size()

while True:
    for _ in range(tamanho):
        for _ in range(tamanho):
            if can_harvest():
                harvest()
            move(North)
        move(East)
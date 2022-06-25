def hanoi(qtt, origem, destino, temp):
    if qtt == 1:
        print(f"Mover de {origem} para {destino}.")
    else:
        hanoi(qtt-1, origem, temp, destino)
        print(f"Mover de {origem} para {destino}.")
        hanoi(qtt-1, temp, destino, origem)


qtt, origem, destino, temp = input().split()
qtt=int(qtt)

hanoi(qtt, origem, destino, temp)
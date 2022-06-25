with open(input()) as file:
    matriz = [list(line.strip()) for line in file]
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        try:
            if matriz[l][c] == "w":
                if matriz[l][c+1] == "a":
                    if matriz[l][c+2] == "l":
                        if matriz[l][c+3] == "l":
                            if matriz[l][c+4] == "y":
                                print(f"{l+1} {c+1} horizontal")
                elif matriz[l+1][c] == "a":
                    if matriz[l+2][c] == "l":
                        if matriz[l+3][c] == "l":
                            if matriz[l+4][c] == "y":
                                print(f"{l+1} {c+1} vertical")
        except:
            pass
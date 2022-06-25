N, M = map(int, input().split())
coordenadasX = 0
coordenadasY = 0
safado_fugiu = False
while N > 0:
    C, D = input().split()
    D = int(D)
    if C == 'N':
        coordenadasY += D
    elif C == 'S':
        coordenadasY -= D
    elif C == 'L':
        coordenadasX += D
    elif C == 'O':
        coordenadasX -= D
    if safado_fugiu == False:
        if (coordenadasX**2 + coordenadasY**2) >= M**2:
            safado_fugiu = True
    N -= 1
if safado_fugiu == True:
    print('sim')
else:
    print('nao')




    

    






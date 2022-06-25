from math import ceil

fil,cad = list(map(int, input().split()))
distancia_max = 0
for f in range(fil):
    fil_n = list(map(int, input().split()))
    distancia_local = 0
    ta_no_canto = True
    for ocupacao in range(cad):
        if fil_n[ocupacao] == 0 and ocupacao != cad-1:
            if ocupacao == 0 or fil_n[ocupacao-1] == 0:
                distancia_local += 1
            else:
                distancia_local += 1
                ta_no_canto = False
        else:
            if ocupacao == cad-1 and fil_n[ocupacao] == 0:
                distancia_local += 1
                ta_no_canto = True
            elif not ta_no_canto:
                distancia_local = ceil(distancia_local/2)
            if distancia_local > distancia_max:
                distancia_max = distancia_local 
            distancia_local = 0

print(distancia_max)
            




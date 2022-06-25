NC = int(input())
for cases in range(NC):
    n, k = map(int, input().split())
    suicida = 0
    lista = []
    for povao in range(n):
        lista.append(povao+1)

    while len(lista) != 1:
        suicida += (k - 1)
        while suicida > (len(lista) -1):
            suicida -= len(lista)
        del lista[suicida]
 
    print(f'Case {cases +1 }: {lista[0]}')




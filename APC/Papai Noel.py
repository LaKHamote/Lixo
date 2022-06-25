garotao = input()
pag = 0
achei = ('nao tem meninos bons no mundo')
while True:
    pag += 1
    k = int(input())
    if k == 0:
        print(achei)
        break
    else:
        while k > 0:
            k -= 1
            if input() == garotao:
                achei = pag





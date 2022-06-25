for _ in range(int(input())):
    conteudo = input()
    estudado = ''
    madrugada = ''
    for _ in range(3):
        estudado += input()
    flag = False
    for c in estudado:
        if c not in conteudo:
            flag = True
            print('You died!')
            break
        conteudo = conteudo.replace(c, '', 1)
    if not flag:
        if conteudo == '':
            print("It's in the box!")
        else:
            print(f'Bora ralar: {"".join(sorted(set(conteudo))) }')
        
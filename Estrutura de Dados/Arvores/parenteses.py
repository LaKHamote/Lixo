def mostra(raiz):
    if raiz is None:
        return print('()')
    print(f'({raiz.dado}',end=f'')
    left = raiz.esq
    if type(left) != int:
        if left != None:
            mostra_aux(left)
        else:
            print(' (',end=')')
    right = raiz.dir
    if type(right) != int:
        if right != None:
            mostra_aux(right)
        else:
            print(' (',end=')')
    print(')',end='') 

def mostra_aux(raiz):
    print(f' ({raiz.dado}',end=f'')
    left = raiz.esq
    if type(left) != int:
        if left != None:
            mostra_aux(left)
        else:
            print(' (',end=')')
    right = raiz.dir
    if type(right) != int:
        if right != None:
            mostra_aux(right)
        else:
            print(' (',end=')')
    print(')',end='')



'''
def mostra_aux(raiz):
    if raiz:
        return f"{raiz.dado} ({mostra_aux(raiz.esq)}) ({mostra_aux(raiz.dir)})"
    return ""

def mostra(raiz):
    print(f"({mostra_aux(raiz)})")

'''

class Arvore():
    def __init__(self, dado):
        self.dado = dado
        self.filhos = []

def mostra(arvore, prop):
    n = 0
    if type(prop) == str:
        global pref
        pref = prop
    else:
        n = prop
    print(f"{n*pref}{arvore.dado}")
    for subArv in arvore.filhos:
        mostra(subArv, n+1)
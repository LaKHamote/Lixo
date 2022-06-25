class ArvoreBinaria():
    def __init__(self, dado, esq=None, dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

def rotaciona_direita(raiz):
    if raiz is None or raiz.esq is None:
        return raiz
    return ArvoreBinaria(raiz.esq.dado, raiz.esq.esq, ArvoreBinaria(raiz.dado, raiz.esq.dir, raiz.dir))

def rotaciona_esq(raiz):
    if raiz is None or raiz.dir is None:
        return raiz
    return ArvoreBinaria(raiz.dir.dado, raiz.dir.dir, ArvoreBinaria(raiz.dado, raiz.dir.esq, raiz.esq))
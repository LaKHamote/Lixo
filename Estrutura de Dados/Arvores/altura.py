def altura(raiz):
    if raiz is None or (raiz.dir is None and raiz.esq is None):
        return 0
    else:
        return 1 + max( altura(raiz.esq), altura(raiz.dir) )

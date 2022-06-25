def mostra_nivel(raiz, n):
    if raiz is None:
        return None
    elif n == 0:
        return mostra(raiz)
    mostra_nivel(raiz.esq, n-1)
    mostra_nivel(raiz.dir, n-1)

def mostra_aux(raiz):
    if raiz:
        return f"{raiz.dado} ({mostra_aux(raiz.esq)}) ({mostra_aux(raiz.dir)})"
    return ""
def mostra(raiz):
    print(f"({mostra_aux(raiz)})")


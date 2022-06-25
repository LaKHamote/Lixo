from sys import setrecursionlimit
setrecursionlimit(10**9)
def buscarArtefato():
    bb8.registrarComoVisitado() 
    resposta = bb8.verificarChao()
    if resposta != None:
        return resposta
    caminhos = [bb8.verificarNorte(), bb8.verificarSul(), bb8.verificarLeste(), bb8.verificarOeste()]
    if caminhos.count(False) == 3:
        index = caminhos.index(True)
        if index == 0:
            bb8.moverNorte()
        elif index == 1:
            bb8.moverSul()
        elif index == 2:
            bb8.moverLeste()
        elif index == 3:
            bb8.moverOeste()
    if bb8.moverNorte():
        if bb8.verificarSeFoiVisitado():
            bb8.moverSul()
    if bb8.moverSul():
        if bb8.verificarSeFoiVisitado():
            bb8.moverNorte()
    if bb8.moverOeste():
        if bb8.verificarSeFoiVisitado():
            bb8.moverLeste()
    if bb8.moverLeste():
        if bb8.verificarSeFoiVisitado():
            bb8.moverOeste()        
    return buscarArtefato()
    
    


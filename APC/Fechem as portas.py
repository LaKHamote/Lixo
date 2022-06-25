import sys
sys.setrecursionlimit(10**6)
N = int(input())
denominador = N
numerador = N
estado_portas = 0 #par = fechado e ímpar = aberto

def fecha_portas(N, numerador, denominador, estado_portas):
    if N == 0:
        return
    if denominador == 1:
        estado_portas += 10**(N - numerador)
        return estado_portas
    else:
        if numerador % denominador != 0:
            return fecha_portas(N, numerador, denominador - 1, estado_portas)
        else:
            estado_portas += 10**(N - numerador)
            return fecha_portas(N, numerador, denominador - 1, estado_portas)

estado_portas_iniciais = fecha_portas(N, numerador, denominador, estado_portas)

def fecha_portas_sequenciais(N, numerador , denominador, estado_portas_iniciais):
    if N == 0:
        return
    if numerador == 1:
        return estado_portas_iniciais
    else:
        estado_portas_alteradas = fecha_portas(N, numerador - 1, denominador - 1, estado_portas_iniciais)
        return fecha_portas_sequenciais(N, numerador - 1, denominador - 1, estado_portas_alteradas)


lista = []
lista = str(fecha_portas_sequenciais(N, numerador , denominador, estado_portas_iniciais))
for lesgo in range(N):
    if (int((lista[lesgo])) + 1) % 2 == 0:
        print(lesgo + 1, end=' ')
    if N == 0:
        break

'''
#bem melhor e certo por algum motivo
n = int(input())
print(*(i ** 2 for i in range(1, int(n ** 0.5) + 1)))
#for i in range(1, int(n ** 0.5) + 1):
    #print(i ** 2, end=' ')
'''







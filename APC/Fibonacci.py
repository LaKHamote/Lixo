'''
fib_salvos = {0: 0, 1: 1}
def fib(n):
    if n in fib_salvos:
        return fib_salvos[n]
    else:
        novo_valor = fib(n-1) + fib(n-2)
        fib_salvos[n] = novo_valor
        return novo_valor

print(fib(int(input())))

'''

fib_salvos = [0, 1]
def fibonacci(n):
    if n == 0:
        return []
    elif n <=2:
        return fib_salvos[:n]
    else:
        for i in range(n-2):
            fib_novo = fib_salvos[-1] + fib_salvos[-2]
            fib_salvos.append(fib_novo)
        return fib_salvos      
print(fibonacci(7))


# n = int(input())
# def fibonacci(n):
#     fib_n = 0
#     fib_n_ant = 0
#     fib_n_antiant = 1
#     while n > 0:
#         fib_n = fib_n_ant + fib_n_antiant
#         fib_n_antiant = fib_n_ant
#         fib_n_ant = fib_n
#         n -= 1
#     print(fib_n)

# fibonacci(n)
    

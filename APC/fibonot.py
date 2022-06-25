k = int(input())
naturais = []
for n in range(10**5):
    naturais.append(n) 


fib_salvos = [0, 1]
def sequencia_fibonacci():
    for _ in range(24):
        fib_novo = fib_salvos[-1] + fib_salvos[-2]
        fib_salvos.append(fib_novo)
    return fib_salvos

fibonacci = sequencia_fibonacci()



def fibonot_function():
    for fib in fibonacci:
        for nat in naturais:
            if nat == fib:
                naturais.remove(nat)
    return naturais                
            

print(*fibonot_function()[:k], sep=', ')

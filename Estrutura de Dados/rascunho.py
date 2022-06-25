fib_salvos = [0, 1]
def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    while len(fib_salvos) < n:
        fib_novo = fib_salvos[-1] + fib_salvos[-2]
        fib_salvos.append(fib_novo)
    return fib_salvos


	
print(fibonacci(7))





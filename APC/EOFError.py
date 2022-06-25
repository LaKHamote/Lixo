def factorial(k):
    fact = 1
    for n in range(k):
        fact*= (n+1) 
    return fact

while True:
    try:
        M, N = map(int, input().split())
        print(factorial(M)+factorial(N))
    except EOFError:
        break

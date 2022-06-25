def primos(n):
    return [ num for num in range(2,n+1) if not 0 in [num%div for div in range(2,num)] ]

print(primos(1000))
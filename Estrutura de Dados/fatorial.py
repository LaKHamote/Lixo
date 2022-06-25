from math import factorial 
pequenos = [1, 1, 2, 6, 24, 120, 720]
for _ in range(int(input())):
    n = int(input())
    fact = [ factorial(i)%2357 for i in list(range(7, n+1)) ]
    if n < 7:
        print(*pequenos)
    else:
        print(*(pequenos+fact))


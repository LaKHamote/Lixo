import math
def primos(n):
    return [num for num in range(2,n+1) if not 0 in [num%div for div in range(2,num)]]

def enesimo_primonacci(seq_primonacci, num):
    for _ in range(num-1):
        seq_primonacci.append(seq_primonacci[-1]+seq_primonacci[-2])
    return seq_primonacci[-1]

    

a, b = map(int, input().split())
num = int(input())
primos = primos(547)
seq_primonacci = [primos[a-1], primos[b-1]]
print(enesimo_primonacci(seq_primonacci, num))

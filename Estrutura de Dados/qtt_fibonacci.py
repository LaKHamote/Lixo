
def fib(n):
    count[n] += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input())
count = {}
for i in range(n+1):
    count[i] = 0

print(f'fibonacci({n}) = {fib(n)}.')
for key in count:
    print(f'{count[key]} chamada(s) a fibonacci({key}).')

def fracoes_periodicas_continuadas_raiz_2_mais_1(N):
    if N == 0:
        return 2
    else:
        return 2 + 1/fracoes_periodicas_continuadas_raiz_2_mais_1(N-1)

N = int(input())
print(f'{(fracoes_periodicas_continuadas_raiz_2_mais_1(N) - 1):.10f}')

'''
a = float(input())
x = float(input())
while True:
    print(x)
    y = (x + a/x) / 2
    if abs(y-x) < 10**(-100):
        break
    x = y
'''
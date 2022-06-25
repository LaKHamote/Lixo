from math import ceil
bytes = int(input())
print(f'Transmitindo {bytes} bytes...')
dowl = 0
tt = 0
while dowl != bytes:
    for _ in range(5):
        tt +=1
        dowl += int(input())
        if dowl == bytes:
            break
    if dowl == 0:
        print('Tempo restante: pendente...')
    elif dowl != bytes:
        print(f'Tempo restante: {ceil(5*(bytes-dowl)/(dowl))} segundos.')
        bytes, dowl = (bytes-dowl), 0
print(f'Tempo total: {tt} segundos.')



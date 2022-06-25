
num = int(input(()))
somatorio = [ 2*n -1 for n in [i+1 for i in range(num)] ]
for i in range(num-1):
    print(f'{somatorio[i]} + soma({somatorio[i+1:]})')
print(somatorio[-1])
print('---------------')
print(f'{num} ** 2 == {sum(somatorio)}')

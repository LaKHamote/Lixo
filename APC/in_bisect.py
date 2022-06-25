def in_bisect(frase, word):
    position = [0,len(frase)-1] #intervalo fechado
    while True:
        try:
            bisection = (len(frase)-1)//2
            if word < frase[bisection].strip():
                position[1] -= (len(frase) - bisection)
                frase = frase[:bisection]
            elif word > frase[bisection].strip():
                frase = frase[(bisection+1):]
                position[0] += (bisection + 1)
            else: #word == frase[bisection]
                print(word == frase[bisection].strip())
                print(position)
                print(sum(position)//2)
                break      
            print('uma vez')
        except IndexError:
            print('Elemento não encontrado.')
            break
    

while True:
    frase = input().split()
    word = input()
    in_bisect(frase, word)
    # frase = list(map(int, input().split(',')))
    # word = int(input())
    # in_bisect(frase, word)



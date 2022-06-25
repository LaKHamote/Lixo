def pattern(n):
    decrescente(n)
    crescente(n)

def decrescente(n):
    print(int(n))
    if n > 0:
        if n % 2 == 0:
            decrescente(n-5)
        else:
            decrescente((n-1)/2)

def crescente(n):
    if n > 0:
        if n % 2 == 0:
           crescente(n-5)
           print(int(n))
        else:
            crescente((n-1)/2)
            print(int(n))

pattern(64)
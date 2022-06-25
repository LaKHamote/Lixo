def divisores(n):
    nume = n 
    deno = n 
    div = 0
    while deno >= 1:
        if nume % deno == 0:
            div += 1 
        deno -= 1
    return div


n = int(input())
maior_div = 1
numero_maior_div = 1
while n > 0:
    div = divisores(n)
    if div >= maior_div:
        maior_div = div
        numero_maior_div = n 
    n -= 1
print(numero_maior_div,end=' ')    
print(maior_div)





  
    


    

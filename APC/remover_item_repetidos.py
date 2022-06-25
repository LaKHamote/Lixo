def remove_duplicatas(lista):
    lista = lista[::-1]
    for item in lista:
        while lista.count(item) > 1:
            lista.remove(item)
    return lista[::-1]

	
print(remove_duplicatas([1,2,3,3,3,3,3,3,3,4,5,6,6,5,4,3,2,1]))

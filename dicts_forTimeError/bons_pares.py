def combinacao_linear_2a2(num):
    return num*(num-1)/2

def busca_pares_bons(dic):
    qtt =0
    for value in dic.values():
        qtt += combinacao_linear_2a2(value)
    return int(qtt)

def count_itens_list(lista):
    dic = dict()
    for item in lista:
        if item not in dic:
            dic[item] = 1
        else:
            dic[item] += 1
    return dic

t = int(input())
lista = list(map(int, input().split()))
print(busca_pares_bons(count_itens_list(lista)))
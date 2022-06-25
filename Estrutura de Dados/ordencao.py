a=[[2,200] , [1, 10000],  [3,20]]
print(sorted(a))

def minha_ordem(i):
    return i[1], i[0] 

print(sorted(a, key=minha_ordem))
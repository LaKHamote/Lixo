def dict_amizades(dupla, hsh):
    amg1, amg2 = dupla
    hsh[amg1].append(amg2)
    hsh[amg2].append(amg1)
    return hsh
        
o,p = input().split()
alunos = input().split()
hsh = {}
for aluno in alunos:
    hsh[aluno] = []
for _ in range(int(p)):
    hsh = dict_amizades(input().split(), hsh)
for aluno in hsh:
    for i in range(len(hsh[aluno])):
        hsh[aluno].extend([kid for kid in hsh[hsh[aluno][i]] if kid != aluno])
for aluno in hsh:
    hsh[aluno] = list(set(hsh[aluno]))
for aluno in hsh:
    for i in range(len(hsh[aluno])):
        hsh[aluno].extend([kid for kid in hsh[hsh[aluno][i]] if kid != aluno])
for aluno in hsh:
    hsh[aluno] = list(set(hsh[aluno]))
for key in sorted(hsh):
    print(f"{key} possui {len(set((hsh[key])))} amigos")
    
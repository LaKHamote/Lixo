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
        amigos_aluno = [kid for kid in hsh[hsh[aluno][i]] if kid != aluno] 
        amigos_amigos_aluno = []
        for kid in hsh[hsh[aluno][i]]:
            if kid != aluno:
                amigos_amigos_aluno.extend(hsh[kid])
                if aluno in hsh[kid]:
                    amigos_amigos_aluno.remove(aluno)
        hsh[aluno].extend(amigos_aluno + amigos_amigos_aluno)
for key in sorted(hsh):
    print(f"{key} possui {len(set((hsh[key])))} amigos")
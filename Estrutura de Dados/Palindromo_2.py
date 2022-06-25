s = input().split()
for w in s:
    palin = []
    if w == w[::-1]:
        pass
    else:
        for i in range(len(w) - 2):
            for j in range(i, len(w) +1)[::-1]:
                if j-i >=3:
                    if w[i:j] == w[i:j][::-1] and not True in [ w[i:j] in p for p in palin ]:
                        palin.append(w[i:j])
        if len(palin) >=2 :
            print(w)

                    







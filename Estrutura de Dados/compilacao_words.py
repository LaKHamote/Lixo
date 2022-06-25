for _ in range(int(input())):
    compac = input()
    descomp = []
    word = ''
    qtt = ''
    for i in range(len(compac)):
        if i == (len(compac) - 1):
            qtt += compac[i]
            descomp.append((word, int(qtt)))
        elif compac[i].isalpha():
            word += compac[i]
        elif compac[i].isnumeric():
            qtt += compac[i]
            if compac[i+1].isalpha():
                descomp.append((word, int(qtt)))
                word = ''
                qtt = ''
    print(*[item[0]*item[1] for item in descomp], sep='')
        
            
                
def soma(x):
    x = str(x)
    if len(x) == 1:
        return x
    else:
        return int(x[0]) + int(soma(x[1:]))

def checagem(x,count):
    somatorio1 = soma(x)
    if int(somatorio1) == x:
        return int(somatorio1), count
    elif len(str(somatorio1)) == 1:
        count += 1
        return int(somatorio1), count
    else:
        count += 1
        return checagem(somatorio1,count)

def tem_q_somar_os_digitos(x):
    return checagem(x,count)

count = 1
print(tem_q_somar_os_digitos(99999999999))
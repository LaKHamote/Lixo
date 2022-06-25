s = input()
tamanho = len(s)
s1 = s[:tamanho//2]
s2 = s[tamanho//2:]
count = 0
while count < len(s1):
    if ord(s1[count]) > ord(s2[count]):
        print(s1 * 2)
        break
    elif ord(s1[count]) < ord(s2[count]):
        print(s2 * 2)
        break
    else:
        count += 1
if count == len(s1):
    print(s)
    
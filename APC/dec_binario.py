from math import isclose

def dec_binario_To_base_10(num):
    num_10 = 0
    for exp in range(len(num)):
        num_10 += (num[exp])*2**((exp+1)*-1)
    return num_10

def base_10_To_dec_binario(num):
    num_dec_2 = []
    if num == 0:
        return [0]
    exp = 1
    while True:
        if isclose(num,0):
            break
        elif num >= 1/(2**exp):
            num -= 1/(2**exp)
            num_dec_2.append(1)
        else:
            num_dec_2.append(0)
        exp += 1
    return num_dec_2

def parte_decimal(num):
    while num >= 1:
        num -= 1
    return num
   
len1, len2 = map(int, input().split())
num1_base2 = list(map(int, input().split()))
num2_base2 = list(map(int, input().split()))

num1_base10 = dec_binario_To_base_10(num1_base2) 
num2_base10 = dec_binario_To_base_10(num2_base2)

resp_base2 = base_10_To_dec_binario(parte_decimal(num1_base10+num2_base10))
print(*resp_base2)

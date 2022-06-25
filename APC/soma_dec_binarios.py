len1, len2 = map(int, input().split())
num1_base2 = list(map(int, input().split()))
num2_base2 = list(map(int, input().split()))

while len(num1_base2) < len(num2_base2):
    num1_base2.append(0)
while len(num2_base2) < len(num1_base2):
    num2_base2.append(0)
carry = 0
resp_invertida = []
for i in range(len(num1_base2)):
    line_addition = num1_base2[(i+1)*(-1)] + num2_base2[(i+1)*(-1)] + carry
    if line_addition < 2:
        resp_invertida.append(line_addition)
        carry = 0
    else:
        resp_invertida.append(line_addition - 2)
        carry = 1
while resp_invertida[0] == 0 and len(resp_invertida)>1:
    resp_invertida.remove(0)

print(*resp_invertida[::-1])



negativo = False
gets = input() 
if gets[0] == '-':
    gets = gets[1:]
    negativo = True
i = len(gets) - 1

puts = ''
if negativo:
    puts += '-'

while i >= 0:
    puts += gets[i]
    i -= 1
print(int(puts))







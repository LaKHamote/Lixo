num, base = map(int, input().split())

def digital_root(num, base):
    if num//base == 0:
        return num
    else:
        return (digital_root(num//base, base))  + (num%base)
  
def checagem():
    talvez = digital_root(num, base)
    if talvez > base:
        return checagem(digital_root(talvez, base))
    else:
        return print(talvez)
    
checagem()
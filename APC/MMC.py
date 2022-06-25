
def mmc():
    a,b = map(int, input().split())
    if a > 0 and b > 0:
        print(int((a*b)/mdc(a,b)))
        mmc()
    else:
        return

def mdc(a,b):
    if b == 0:
        return a
    return mdc(b,a%b)

mmc()
'''
calcula mdc para 3 variáveis
def mdc(a,b,c):
    if b == 0:
        return mdc_3(a,b,c)
    return mdc(b,a%b,c)
    
def mdc_3(a,b,c):
    if c == 0:
        return a
    return mdc_3(c,b,a%c)
'''


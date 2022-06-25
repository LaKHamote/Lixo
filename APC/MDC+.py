def mdc(a,b,c):
    if c == 0:
        return a 
    elif b == 0:
        return mdc(c,b,a%c)
    elif b != 0:
        return mdc(b,a%b,c)

print(mdc(10,5,25))
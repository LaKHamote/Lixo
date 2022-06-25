def cond(p,q,r):
    if p :
        if q :
            if r :
                return True
            else:
                return False
        else:
            return True
    else:
        if r :
            return True
        else:
            return False


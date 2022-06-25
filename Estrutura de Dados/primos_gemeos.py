def primos_gemeos(n):
    resp = []
    primo = []
    num = 2
    while len(resp) < n:
        if 0 not in [num%div for div in range(2,num)]:
            primo.append(num)
        if len(primo) == 2:
            ultimo = primo[1]
            if ultimo - primo[0] == 2:
                resp.append(tuple(primo))
            primo = [ultimo]
        num += 1
    return resp


print(primos_gemeos(10))
            
     


            
    
hsh = {}
for _ in range(4):
    a = input() 
    tel = input() 
    cost = int(input()) 
    if tel not in hsh:
        hsh[tel] = [-1, cost]
    else:
        if cost < hsh[tel][1]:
            hsh[tel][1] = cost
        hsh[tel][0] -= 1
print(sorted(hsh.items(), key= lambda x:x[1])[0][0])


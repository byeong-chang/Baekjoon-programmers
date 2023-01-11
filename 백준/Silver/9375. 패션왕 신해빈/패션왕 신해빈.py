import sys
T =int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    clothes = dict()    
    for j in range(n):
        name,ctype = sys.stdin.readline().split()
        if ctype in clothes:
            clothes[ctype].append(name)
        else: clothes[ctype] = [name]
    
    
    if len(clothes.keys()) == 1 :
        total = n
    else :
        total = -1
        mux =1 
        for i in clothes:
            mux *= len(clothes[i])+1
        total +=mux
    print(total)
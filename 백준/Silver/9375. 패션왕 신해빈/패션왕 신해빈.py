# 코드 단축이 가능할 것 같아 추가를 해보았다.

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
    
    #수정코드 계산부에 if else 문이 필요없음을 느낌
    total=1
    for i in clothes:
        total *= len(clothes[i])+1
    print(total-1)
    
"""     이전코드
    if len(clothes.keys()) == 1 :
        total = n
    else :
        total = -1
        mux =1 
        for i in clothes:
            mux *= len(clothes[i])+1
        total +=mux
    print(total)"""

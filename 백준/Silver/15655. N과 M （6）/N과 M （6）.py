'''
조합 출력문제
'''

import sys

def input():
    return sys.stdin.readline()

N,M = map(int,input().split())  
Ns = sorted(list(map(int,input().split())))
select = [0 for _ in range(M)]

def comb(idx,sidx):
    if sidx == M:
        print(*select)
        return
    
    if idx == N:
        return
    
    select[sidx] = Ns[idx]
    comb(idx+1,sidx+1)
    comb(idx+1,sidx)
    

comb(0,0)

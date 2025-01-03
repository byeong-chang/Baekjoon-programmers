'''
조합 출력문제
'''

import sys

def input():
    return sys.stdin.readline()

N,M = map(int,input().split())  
arr = [i for i in range(1,N+1)]
select = [0 for _ in range(M)]

def comb(idx, sidx):
    if sidx == M:
        print(*select)
        return
    
    if idx == N:
        return

    select[sidx] = arr[idx]
    comb(idx+1, sidx+1)
    comb(idx+1, sidx)
    
comb(0,0)
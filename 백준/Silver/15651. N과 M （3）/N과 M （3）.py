'''
중복 순열 출력문제
'''

import sys

def input():
    return sys.stdin.readline()

N,M = map(int,input().split())  
arr = [i for i in range(1,N+1)]
select = [0 for _ in range(M)]

def perm(depth):
    if depth == M:
        print(*select)
        return 
    
    for i in range(N):
        select[depth] = arr[i]
        perm(depth+1)


perm(0)
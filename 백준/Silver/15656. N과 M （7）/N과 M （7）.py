'''
중복순열 출력문제
'''

import sys

def input():
    return sys.stdin.readline()

N,M = map(int,input().split())  
Ns = sorted(list(map(int,input().split())))
select = [0 for _ in range(M)]

def perm(depth):
    if depth == M:
        print(*select)
        return

    for i in range(N):
        select[depth] = Ns[i]
        perm(depth+1)

perm(0)
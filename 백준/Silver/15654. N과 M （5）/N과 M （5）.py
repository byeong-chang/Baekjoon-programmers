'''
순열 출력문제
'''

import sys

def input():
    return sys.stdin.readline()

N,M = map(int,input().split())  
Ns = sorted(list(map(int,input().split())))
select = [0 for _ in range(M)]
check = [0 for _ in range(N)]

def perm(depth):
    if depth == M:
        print(*select)
        return

    for i in range(N):
        if not check[i]:
            select[depth] = Ns[i]
            check[i] = 1
            perm(depth+1)
            check[i] = 0

perm(0)
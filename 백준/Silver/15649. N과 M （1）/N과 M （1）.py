'''
순열 출력문제
'''

def input():
    return sys.stdin.readline()
import sys


N,M = map(int,input().split())  
arr = [i for i in range(1,N+1)]
select = [0 for _ in range(M)]
check = [0 for _ in range(N)]

def perm(depth):
    if depth == M:
        print(*select)
        return
    
    for i in range(N):
        if not check[i]:
            check[i] = 1
            select[depth] = arr[i]
            perm(depth+1)
            check[i] = 0
perm(0)
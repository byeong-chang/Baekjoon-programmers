
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def perm(depth):
    global answer
    if depth == n:
        answer.append(sel[::])
        return
        
    for i in range(m):
        if not check[i]:
            check[i] = True
            sel[depth] = lst[i]
            perm(depth+1)
            check[i] = False

m,n = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
sel = [0 for _ in range(n)]
check = [0 for _ in range(m)]
answer = []

perm(0)

for val in sorted(list(set([tuple(val) for val in answer]))):
    print(*val)

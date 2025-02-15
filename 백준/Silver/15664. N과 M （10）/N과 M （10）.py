
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def perm(depth):
    if depth == m:
        for i in range(m-1):
            if sel[i] > sel[i+1]:
                return
        else:
            answer.append(sel[::])
            return

    for i in range(n):
        if not check[i]:
            check[i] = True
            sel[depth] = lst[i]
            perm(depth+1)
            check[i] = False

n,m = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
answer = []
check = [0 for _ in range(n)]
sel = [0 for _ in range(m)]

perm(0)
for val in sorted(list(set([tuple(val) for val in answer]))):
    print(*val)
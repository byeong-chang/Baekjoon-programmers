
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

n,m = map(int,input().split())
lst = list(map(int,input().split()))
sel = [0 for _ in range(m)]
answer = []

def perm(depth):
    if depth == m:
        for k in range(m-1):
            if sel[k] > sel[k+1]:
                return
        answer.append(sel[::])
        return

    for i in range(n):
        sel[depth] = lst[i]
        perm(depth+1)


perm(0)

for val in sorted(list(set([tuple(v) for v in answer]))):
    print(*val)
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

count = 0
N,M = map(int, input().split())
lst = [[] for _ in range(N+1)]
sel = [0] * 3

for _ in range(M):
    a,b = map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)

def combination(idx, sidx):
    global count
    
    if sidx == 3:
        count +=1
        return

    if idx == N:
        return
    
    flag = True
    for i in range(0, sidx):
        if sel[i] in lst[idx + 1]:
            flag = False
            break
    if flag:
        sel[sidx] = idx + 1
        combination(idx+1, sidx+1)
    combination(idx+1, sidx)

combination(0,0)
print(count)

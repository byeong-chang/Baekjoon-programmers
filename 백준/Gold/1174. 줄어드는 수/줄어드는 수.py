import sys
from collections import deque
import math
def input():
    return sys.stdin.readline().rstrip()

N = int(input())-1
arr = [str(k) for k in range(9,-1,-1)]
count = deque([])


def comb(sidx,idx):
    
    if sidx == i:
        decrease_check(sel)
        return

    if idx < 10 and not check[idx]:
        sel[sidx] = arr[idx]
        comb(sidx+1,idx+1)
        comb(sidx,idx+1)


def decrease_check(lst):
    global count
    for j in range(len(sel)-1):
        if sel[j] < sel[j+1]:
            break
    else:
        count.appendleft(int("".join(lst)))


for i in range(1,12):
    if len(count) > N:
        print(count[N])
        break
    else: 
        N -= len(count)
        count = deque([])

    sel = [0] * i
    check = [0] * 10
    comb(0,0)
else:
    print(-1)

import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

n,k,q,m = map(int,input().split())
sleeps = list(map(int,input().split()))
starts = list(map(int,input().split()))
attendance = [False for _ in range(n+3)]

for start in starts:
    if start not in sleeps:
        for i in range(start,n+3,start):
            attendance[i] = True

for sleep in sleeps:
    attendance[sleep] = False

for _ in range(m):
    s,e = map(int,input().split())
    temp = attendance[s:e+1]
    print(len(temp) - sum(temp))
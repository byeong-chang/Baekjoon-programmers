
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

n,m = map(int,input().split())
trains = [deque([0 for _ in range(20)]) for _ in range(n+1)]
for _ in range(m):
    op = list(map(int,input().split()))
    if op[0] == 1:
        trains[op[1]][op[2]-1] = 1
    elif op[0] == 2:
        trains[op[1]][op[2]-1] = 0
    elif op[0] == 3:
        trains[op[1]].appendleft(0)
        trains[op[1]].pop()
    else:
        trains[op[1]].append(0)
        trains[op[1]].popleft()

answer = set([tuple(val) for val in trains[1:]])
print(len(answer))

import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

n,m,k,x = map(int,input().split())
queue = deque([[x,0]])
maps = [[] for _ in range(n+1)]
minDistance = [k+1 for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    maps[a].append(b)

while queue:
    current,distance = queue.popleft()

    if distance > k:
        continue

    if minDistance[current] > distance:
        minDistance[current] = distance
        for vertex in maps[current]:
            queue.append([vertex,distance+1])

flag = True
for i in range(1,len(minDistance)):
    if minDistance[i] == k:
        print(i)
        flag = False

if flag : print(-1)
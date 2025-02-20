import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
# map(int,input().split())
n,m = map(int,input().split())
linkedList = [[] for _ in range(n+1)]
count = [0 for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    linkedList[b].append(a)

def check(queue):
    total = 1
    visited = [False for _ in range(n+1)]
    visited[queue[0]] = True

    while queue:
        current = queue.popleft()

        for v in linkedList[current]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
                total +=1

    return total

answer,maxVal = [],0
for i in range(1,n+1):
    total = check(deque([i]))
    if total > maxVal:
        maxVal = total
        answer = [i]
    elif total == maxVal:
        answer.append(i)

answer.sort()
for v in answer: print(v)
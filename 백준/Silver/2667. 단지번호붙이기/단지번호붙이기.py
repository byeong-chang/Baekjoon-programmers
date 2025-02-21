import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
# map(int,input().split())

n = int(input())
lst = [list(map(int,input())) for _ in range(n)]
visited = [[False] * n  for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer = []

def dfs(stack):
    count = 0
    while stack:
        x,y = stack.pop()
        count+=1
        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            if (ddx < n and ddy < n and ddx > -1 and ddy > -1) and lst[ddx][ddy]and not visited[ddx][ddy]:
                visited[ddx][ddy] = True
                stack.append([ddx,ddy])
    return count

for i in range(n):
    for j in range(n):
        if not visited[i][j] and lst[i][j]:
            visited[i][j] = True
            temp = dfs([[i,j]])
            if temp:
                answer.append(temp)

print(len(answer))
for v in sorted(answer):
    print(v)
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
    
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
queue = deque([])
found = False  

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            queue.append([i, j])
            found = True  
            break
    if found:  
        break

while queue:
    x,y = queue.popleft()

    for k in range(4):
        ddx = x + dx[k]
        ddy = y + dy[k]

        if ddx < n and ddy < m and ddx > -1 and ddy > -1:
            if not visited[ddx][ddy] and graph[ddx][ddy] != 0:
                queue.append([ddx,ddy])
                visited[ddx][ddy] = visited[x][y] +1

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            print(-1,end = " ")
        elif graph[i][j] == 2:
            print(0, end = " ")
        else: 
            print(visited[i][j], end = " ")
    print()

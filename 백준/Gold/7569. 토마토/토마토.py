import sys
from collections import deque

m,n,h = map(int,input().split())
graph = []
for i in range(h):
    graph.append([list(map(int,input().split())) for j in range(n)])
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

Q = deque()
for i in range(len(graph)):
    for j in range(len(graph[0])):
        for k in range(len(graph[0][0])):
            if graph[i][j][k] == 1:
                Q.append([i,j,k])
# i j k = h, m, n
def bfs():
    while Q:
        z,x,y = Q.popleft()
        for i in range(6):
            nz,nx,ny = z+dz[i], x + dx[i], y + dy[i]
            if nz <0 or ny <0 or nx<0 or nz>=h or nx>=n or ny >= m:
                continue
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                Q.append([nz,nx,ny])

bfs()
days = 0
for lst in graph:
    for i in lst:
        for j in i:
            if j == 0:
                print(-1)
                exit()
            else:
                if j > days:
                    days = j
print(days-1)
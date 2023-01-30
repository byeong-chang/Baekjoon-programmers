import sys
from collections import deque

m,n= map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

Q = deque()
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == 1 :
            Q.append([i,j])
def bfs():
    while Q:
        x,y = Q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if nx>=n or nx<0 or ny <0 or ny >=m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                Q.append([nx,ny])

bfs()

days =  0
for line in graph:
    for j in line:
        if j == 0:
            print(-1)
            exit()
        else: 
            if j> days:
                days = j
print(days-1)
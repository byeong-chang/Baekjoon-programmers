import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())
maze = [list(map(int,sys.stdin.readline().strip())) for i in range(N)]
visited = [ [False]*M for i in range(N)]
Q = deque()
Q.append([0,0])
dx = [1,-1,0,0]
dy = [0,0,1,-1]
while Q:
    x,y = Q.popleft()
    if maze[x][y] >= 1:
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if not(nx>=N or ny>=M or nx<=-1 or ny<=-1) and maze[nx][ny] >= 1 and not visited[nx][ny]:
                Q.append([nx,ny])
                maze[nx][ny] = maze[x][y]+1
                visited[nx][ny] = True
print(maze[N-1][M-1])
import sys
from collections import deque
N = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().strip()))for i in range(N)]
visited = [[False]*N for i in range(N)]
count = 0
count_lst = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def BFS(a,b):
    Q= deque()
    Q.append([a,b])
    cnt = 0
    while Q:
        cnt+=1
        x,y = Q.popleft()
        for i in range(4):
            nx,ny = x+dx[i] , y+dy[i]
            if not(nx<=-1 or ny<=-1 or nx>=N or ny>=N):
                if visited[nx][ny] == False and graph[nx][ny] == 1:
                    Q.append([nx,ny])
                    visited[nx][ny] = True
    return cnt

for x in range(N):
    for y in range(N):
        if visited[x][y] == False and graph[x][y] == 1:
            visited[x][y] = True
            count_lst.append(BFS(x,y))
            count+=1

count_lst.sort()
print(count)
for i in count_lst:
    print(i)
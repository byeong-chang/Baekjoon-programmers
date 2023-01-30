import sys
sys.setrecursionlimit(100000)
N = int(input())

graph = [input() for i in range(N)]
visited = [[False] *N for i in range(N)]

def dfs(x,y,value):
    if (x >= N or y >= N or x < 0 or y < 0) :
        return
    if value == graph[x][y] and not visited[x][y]:
        visited[x][y] = True
        dfs(x-1,y,value)
        dfs(x+1,y,value)
        dfs(x,y-1,value)
        dfs(x,y+1,value)

count_1 = 0 
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i,j,graph[i][j])
            count_1+=1
count_2 = 0
visited = [[False] *N for i in range(N)]
for line in range(N):
    graph[line] = graph[line].replace('R','G')

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i,j,graph[i][j])
            count_2+=1
print(count_1,count_2)
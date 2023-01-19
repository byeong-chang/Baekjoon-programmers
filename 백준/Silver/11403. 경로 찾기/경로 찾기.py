import sys

N = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().split())) for i in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if (graph[i][k] + graph[k][j]) >= 2:
                graph[i][j] = 1
for i in graph:
    for j in i:
        print(j,end=' ')
    print()
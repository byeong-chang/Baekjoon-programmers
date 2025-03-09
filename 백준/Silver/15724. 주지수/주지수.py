import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
    
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

cumulatedGraph = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            cumulatedGraph[i][j] = graph[i][j]
        elif i == 0:
            cumulatedGraph[i][j] = graph[i][j] + cumulatedGraph[i][j-1]
        elif j == 0:
            cumulatedGraph[i][j] = graph[i][j] + cumulatedGraph[i-1][j]
        else: 
            cumulatedGraph[i][j] = graph[i][j] + cumulatedGraph[i][j-1] + cumulatedGraph[i-1][j] - cumulatedGraph[i-1][j-1]

k = int(input())
for _ in range(k):
    x1,y1,x2,y2 = [v-1 for v in list(map(int,input().split()))]
    if x1 == 0 and y1 == 0:
        print(cumulatedGraph[x2][y2])
    elif x1 == 0:
        print(cumulatedGraph[x2][y2] - cumulatedGraph[x2][y1-1])
    elif y1 == 0:
        print(cumulatedGraph[x2][y2] - cumulatedGraph[x1-1][y2])
    else:
        print(cumulatedGraph[x2][y2] + cumulatedGraph[x1-1][y1-1] - cumulatedGraph[x1-1][y2] - cumulatedGraph[x2][y1-1])


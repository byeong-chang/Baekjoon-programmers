from collections import deque
import sys
read = sys.stdin.readline


n,m,v = map(int,read().split())
graph = [[0]*(n+1) for i in range(n+1)]
visit_list = [0] * (n+1)
visit_list2 = [0] * (n+1)

for i in range(m):
    a,b = map(int, read().split())
    graph[a][b] = graph[b][a] = 1

dq = deque()
def bfs(vertex):
    dq.append(vertex)
    while dq:
        v = dq.popleft()
        print(v,end=" ")
        visit_list[v] = 1
        for i in range(1,n+1):
            if visit_list[i] == 0 and graph[v][i] ==1 and i not in dq:
                dq.append(i)

def dfs(v):
    visit_list2[v] = 1
    print(v,end=" ")
    for i in range(1,n+1):
        if visit_list2[i] == 0 and graph[v][i] ==1:
            dfs(i)

dfs(v)
print()
bfs(v)
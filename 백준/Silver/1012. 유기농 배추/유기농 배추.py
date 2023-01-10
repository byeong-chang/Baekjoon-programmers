import sys
sys.setrecursionlimit(10**6)
T = int(sys.stdin.readline())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    if x <= -1 or y <= -1 or x>=M or y>= N:
        return False
    
    if baechu_lst[x][y] == 1:
        baechu_lst[x][y] = 0
        for i in range(4):
            bfs(x+dx[i],y+dy[i])

for i in range(T):
    M,N,k = map(int,sys.stdin.readline().split())
    baechu_lst = [[0]*N for i in range(M)]
    for j in range(k):
        x,y = map(int,sys.stdin.readline().split())
        baechu_lst[x][y] = 1

    count = 0
    for j in range(M):
        for k in range(N):
            if baechu_lst[j][k] == 1:
                bfs(j,k)
                count +=1
    print(count)
N,M = map(int,input().split())
friendship = [[N for i in range(N)] for _ in range(N)]
for i in range(M):
    x,y = map(int,input().split())
    friendship[x-1][y-1] = 1
    friendship[y-1][x-1] = 1

for k in range(N): # 경로 for 문이 가장 상위 단계여야 누락되지 않는다고 하네요..
    for i in range(N):
        for j in range(N):
            if i == j : 
                friendship[i][j]=0
            else:
                friendship[i][j] = min(friendship[i][k]+friendship[k][j],friendship[i][j])

FW_len = []
for i in friendship:
    FW_len.append(sum(i))
print(FW_len.index(min(FW_len))+1)
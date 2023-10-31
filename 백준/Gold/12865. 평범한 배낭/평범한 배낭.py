N,K = list(map(int,input().split()))
dp = [[0]*(K+1) for _ in range(N+1)]
lst = [[0,0]]
for i in range(N):
    lst.append(list(map(int,input().split())))
for i in range(1,N+1):
    for j in range(1,K+1):
        w,v =lst[i]
        if w >j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], (v + dp[i-1][j-w]))
print(dp[-1][-1])

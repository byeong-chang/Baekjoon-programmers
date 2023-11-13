def solution(x, y, n):
    dp = [ -1 for i in range(y*3+1)]
    dp[x] = 0
    for i in range(x,y):
        if dp[i] == -1:
            pass
        else:
            if dp[i+n] != -1:
                dp[i + n] = min(dp[i]+1,dp[i+n])
            else: dp[i+n] = dp[i]+1
            
            if dp[i*2] != -1:
                dp[i*2] = min(dp[i*2], dp[i]+1)
            else: dp[i*2] = dp[i]+1
            
            if dp[i*3] != -1:
                dp[i*3] = min(dp[i*3] , dp[i]+1)
            else: dp[i*3] = dp[i]+1
            
    return dp[y]
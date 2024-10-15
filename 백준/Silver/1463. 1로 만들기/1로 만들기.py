import sys

def input():
    return sys.stdin.readline().rstrip()
    

n = int(input())
dp = [0,0,1,1] 
for i in range(4,n+1):
    dps = []
    if i % 3 == 0:
        dps.append(dp[i//3])
    if i % 2 == 0:
        dps.append(dp[i//2])
    dps.append(dp[i-1])
    dp.append(min(dps) + 1)
print(dp[n])
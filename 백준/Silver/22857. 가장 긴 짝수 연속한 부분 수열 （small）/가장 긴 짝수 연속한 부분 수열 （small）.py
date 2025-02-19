
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
# map(int,input().split())
n,k = map(int,input().split())
lst = [val%2==0 for val in list(map(int,input().split()))]
lst.insert(0,0)
dp = [[0]*(k+2) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+2):
        if lst[i]: dp[i][j] = dp[i-1][j] +1
        else: dp[i][j] = dp[i-1][j-1]

answer = 0
for v in dp:
    answer = max(answer,max(v))

print(answer)
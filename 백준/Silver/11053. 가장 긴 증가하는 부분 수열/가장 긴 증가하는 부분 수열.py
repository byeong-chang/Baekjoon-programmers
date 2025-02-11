
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
    

N = int(input())
lst = list(map(int,input().split()))
dp = [0 for _ in range(N+1)]

for i in range(N):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp)+1)
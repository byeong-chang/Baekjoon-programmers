import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
# map(int,input().split())

n = int(input())
dp = [0 for _ in range(n)]
lst = [int(input()) for _ in range(n) ]
if n < 3:
    print(sum(lst))
else:
    dp[0] = lst[0]
    dp[1] = dp[0] + lst[1] 
    dp[2] = max(dp[1],dp[0] + lst[2], lst[1]+lst[2])
    for i in range(3,n):
        dp[i] = max(dp[i-1], dp[i-2] + lst[i], dp[i-3]+lst[i-1] + lst[i])
    print(dp[-1])
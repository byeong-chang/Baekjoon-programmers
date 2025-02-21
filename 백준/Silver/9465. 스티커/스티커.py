import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
# map(int,input().split())
t = int(input())

# n이 충분히 크기 떄문에 dp로 접근해야함.
for i in range(t):
    n = int(input())
    points = [list(map(int,input().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(2)]
    # 구현 공식은 1열일때 2열일때로 나눠서 계산
    # 1열 구현
    
    dp[0][0] = points[0][0]
    dp[1][0] = points[1][0]
    if n ==1: 
        print(max(dp[0][-1],dp[1][-1]))
        continue

    dp[0][1] = points[1][0] + points[0][1]
    dp[1][1] = points[0][0] + points[1][1]
    if n == 2 : 
        print(max(dp[0][-1],dp[1][-1]))
        continue
    else:
        for j in range(2,n):
            dp[0][j] = max(dp[1][j-1], dp[1][j-2])+points[0][j]
            dp[1][j] = max(dp[0][j-1], dp[0][j-2])+points[1][j]
        
        print(max(dp[0][-1],dp[1][-1]))
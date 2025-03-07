import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
orders = [list(map(int,input().split())) for _ in range(m)]
dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i==0 and j==0:
            dp[0][0] = graph[0][0]
        if i == 0:
            dp[i][j] = dp[i][j-1] + graph[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j] + graph[i][j]
        else:
            dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + graph[i][j]

for order in orders:
    x1, y1, x2, y2 = order[0]-1, order[1]-1, order[2]-1, order[3]-1
    if x1 == 0 and y1 == 0:
        print(dp[x2][y2])
    elif x1 == 0:
        print(dp[x2][y2] - dp[x2][y1-1])
    elif y1 == 0:
        print(dp[x2][y2] - dp[x1-1][y2])
    else:
        print(dp[x2][y2] - dp[x1-1][y2]  - dp[x2][y1-1] + dp[x1-1][y1-1])
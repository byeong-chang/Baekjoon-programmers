import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
# map(int,input().split())

n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]

#bfs, dp로 풀 예정
queue = deque([(0,0)])
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        current = maps[i][j]

        if current == 0 or (i==n-1 and j == n-1):
            continue

        if i+current < n:
            dp[i+current][j] += dp[i][j] 
        
        if j + current < n:
            dp[i][j+current] += dp[i][j]

print(dp[-1][-1])

import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
    
N = int(input())
lst = list(map(int,input().split()))
dp = [0 for _ in range(N)]
dp[0] = lst[0]

for i in range(1,N):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i],dp[j] + lst[i])
        else: dp[i] = max(dp[i],lst[i])

print(max(dp))

# else 안쓰면 생기는 반례 : 10 5 4 3 4 5
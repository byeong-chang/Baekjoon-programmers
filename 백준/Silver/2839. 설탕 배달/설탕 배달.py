import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

'''그리디 문제는 가능한 경우의 수가 배수여야하는 것으로 알고있다.
예를들어 문제는 3,5기 때문에 불가능하고, 3,6이었다면 그리디로 풀 수 있을텐데 했다.
그래서 DP로 풀기로 접근하였다.'''

n = int(input())
dp = [5000 for _ in range(5001)]
dp[3],dp[5] = 1,1

for i in range(6,n+1):
    dp[i] = min(dp[i-3], dp[i-5])+1

if dp[n] > 4999:
    print(-1)
else:
    print(dp[n])

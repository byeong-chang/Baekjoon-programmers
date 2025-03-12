import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n-1)]
k = int(input())
# 0,1 번째 dp 설정
dp = [0] * n
if n > 1:
    dp[1] = lst[0][0]
    
for i in range(2,n):
    dp[i] = min(dp[i-1] + lst[i-1][0], dp[i-2] + lst[i-2][1])

# 매우 큰 점프 사용하지 않는 경우
answer = [dp[-1]]

# 매우 큰 점프 사용
for j in range(3,n):
    # 초기 값 두개 설정
    temp = [dp[j-3] + k]
    # 마지막에 도착할 때 매우 큰 점프 사용
    if j+1 != n:
        temp.append(temp[0]+lst[j][0])

    for m in range(j+2,n):
        temp.append(min(temp[-1] + lst[m-1][0], temp[-2] + lst[m-2][1]))

    answer.append(temp[-1])
print(min(answer))

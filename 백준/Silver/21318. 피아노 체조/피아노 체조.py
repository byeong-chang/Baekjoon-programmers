import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
nums = list(map(int,input().split()))
sums = [0] * (n+1)

for i in range(0,n-1):
    if nums[i] > nums[i+1]:sums[i+2] = sums[i+1] +1
    else: sums[i+2] = sums[i+1]

q = int(input())
for _ in range(q):
    x,y = map(int,input().split())
    print(sums[y]-sums[x])

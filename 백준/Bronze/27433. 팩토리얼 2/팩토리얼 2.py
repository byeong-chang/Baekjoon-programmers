import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
total = 1
for i in range(2,n+1):
    total*= i
print(total)
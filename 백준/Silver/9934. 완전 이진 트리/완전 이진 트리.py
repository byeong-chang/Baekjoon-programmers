import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
# map(int,input().split())
n = int(input())
depths = {i : [] for i in range(n)}
lst = list(map(int,input().split()))
# 중위순회를 해독하는 문제
# 데이터를 반으로 자른다(1이 될 때 까지)

def slice (depth,temp):
    if len(temp) == 1:
        depths[depth].append(temp[0])
    else:
        length = len(temp)//2
        slice(depth+1,temp[:length])
        depths[depth].append(temp[length])
        slice(depth+1,temp[length+1:])

slice(0,lst)
for val in depths.values():
    print(*val)
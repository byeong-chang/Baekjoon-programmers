import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

'''n이 굉장히 작은 문제라 정렬하고 수학적으로 품
NlogN + N '''

N = int(input())
ropes = []
for _ in range(N):
    ropes.append(int(input()))
ropes.sort(reverse = True)

answer = -1
for i,rope in enumerate(ropes):
    temp =  rope * (i+1) 
    if temp > answer:
        answer = temp
print(answer)
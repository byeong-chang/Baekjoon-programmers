
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

''' -1 하고 시작
0 될떄까지 계산
n 은 n//2 해서 저장
n%2 했을때 홀수면 바뀐거 짝수면 안바뀐거
'''

n = int(input())-1
flag = 0
while n > 0:
    temp = n%2
    n//=2

    if temp == 1:
        flag = (flag+1)%2

print(flag)

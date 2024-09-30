import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

'''2^63을 제곱근해보니 대충 30억정도 나오더군요
brute force는 택도 없겠다 싶어서 이분탐색으로 시도하였습니다.
파이썬은 자료형 크기는 신경 안써도 되어서 편하긴 하네요'''

n = int(input())
start,end = 0, n

while start < end:
    middle = (start + end) // 2
    
    if middle ** 2 >= n: end = middle
    else: start = middle + 1
print(end)
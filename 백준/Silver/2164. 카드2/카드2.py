import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

'''데이터가 앞에서 나가고 뒤에 추가되므로 queue사용'''

N = int(input())
Q = deque([i for i in range(1,N+1)])
while len(Q) != 1:
    Q.popleft()
    Q.append(Q.popleft())
print(Q[0])

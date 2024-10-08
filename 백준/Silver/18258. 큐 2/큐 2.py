
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

q = deque()
n = int(input())
for _ in range(n):
    call = input()
    if 'push' in call:
        call, num = call.split()

    if call == 'push':
        q.append(int(num))
    elif call == "pop":
        if len(q) == 0: print(-1)
        else: print(q.popleft())
    elif call == "size":
        print(len(q))
    elif call == "empty":
        if len(q) == 0: print(1)
        else: print(0)
    elif call == "front":
        if len(q) == 0: print(-1)
        else: print(q[0])
    elif call == "back":
        if len(q) == 0: print(-1) 
        else: print(q[-1])
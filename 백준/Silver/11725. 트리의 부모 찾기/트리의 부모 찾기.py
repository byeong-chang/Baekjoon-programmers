
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
    

'''
    bfs로 풀면 된다.
'''

N = int(input())
answer = [0] * (N+1)
check =[False] * (N+1)
linked = {i : [] for i in range(1,N+1)}


for _ in range(N-1):
    a,b = map(int,input().split())
    linked[a].append(b)
    linked[b].append(a)

queue = deque([1])
check[1] = True

while queue:
    current = queue.popleft()
    for val in linked[current]:
        if not check[val]:
            queue.append(val)
            check[val] = True
            answer[val] = current


for i in range(2,N+1):
    print(answer[i])
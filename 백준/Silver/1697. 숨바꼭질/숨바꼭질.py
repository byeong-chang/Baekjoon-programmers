import sys
from collections import deque
N,K = map(int,sys.stdin.readline().split())
Max = 100000
move_cnt = [0] * (Max+1)
Q = deque()
Q.append(N)
while Q:
    cur = Q.popleft()
    if cur == K:
        print(move_cnt[cur])
        break
    for i in [cur+1,cur-1,cur*2]:
        if 0<= i <= Max and not move_cnt[i]:
            move_cnt[i] = move_cnt[cur]+1
            Q.append(i)
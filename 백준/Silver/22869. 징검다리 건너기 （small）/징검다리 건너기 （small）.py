import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

n,k = map(int,input().split())
lst = list(map(int,input().split()))
visited = [False] * n
visited[0] = True
queue = deque([0])

while queue:
    i = queue.popleft()
    
    for j in range(i+1,i+k+1):
        if j < n and (j-i) * (1+ abs(lst[j]-lst[i])) <= k and not visited[j]:
            queue.append(j)
            visited[j] = True
            if j == n-1:
                print("YES")
                exit()
else:
    print("NO")
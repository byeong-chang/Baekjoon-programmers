import sys
from heapq import heappush , heappop
T = int(sys.stdin.readline())
for i in range(T):
    minheap ,maxheap = [], []
    visited = [False] * 1000001 
    K = int(sys.stdin.readline())
    lst = [sys.stdin.readline().split() for j in range(K)]
    
    for key in range(len(lst)):
        op = lst[key]
        if op[0] == 'I':
            heappush(minheap,(int(op[1]),key)) # min heap으로 저장
            heappush(maxheap, (-int(op[1]),key)) # max heap으로 저장
            visited[key] =  True
        else:
            if op[1] == '-1':
                while minheap and not visited[minheap[0][1]]:
                    heappop(minheap)
                if minheap:
                    visited[minheap[0][1]] = False
                    heappop(minheap)
            else:
                while maxheap and not visited[maxheap[0][1]]:
                    heappop(maxheap)
                if maxheap:
                    visited[maxheap[0][1]] = False
                    heappop(maxheap)
    while minheap and not visited[minheap[0][1]]:
        heappop(minheap)
    while maxheap and not visited[maxheap[0][1]]:
        heappop(maxheap)

    try:
        print(-maxheap[0][0], minheap[0][0])
    except IndexError:
        print('EMPTY')
import sys
from heapq import heappush
from heapq import heappop

N = int(sys.stdin.readline())
heap = []
for i in range(N):
    value = int(sys.stdin.readline())
    if value == 0:
        try:
            print(heappop(heap)[1])
        except:
            print(0)
    else:
        heappush(heap,(abs(value),value))
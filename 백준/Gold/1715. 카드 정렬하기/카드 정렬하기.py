from heapq import heappop
from heapq import heappush

N = int(input())
heap = []
sums = 0
for i in range(N):
    heappush(heap,int(input()))
while len(heap) != 1 :
    x = heappop(heap)
    y = heappop(heap)
    sums += (x+y)
    heappush(heap,x+y)

print(sums)
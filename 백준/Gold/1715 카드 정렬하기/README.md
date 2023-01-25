```python

'''
정렬하고 nlogn
2개로 맞추고  1
2개씩 묶어서 더해 n
Nlogn +N 
시간초과 안날듯?

인줄 알았으나 문제를 잘못읽었었네.

sort 하고                nlogn
~값 1개 남을때 까지 반복

작은값 2개 뽑아서 더하고  1
정렬되게끔 저장.          logn
~ 
minheap 사용하여 풀이함
'''

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
```

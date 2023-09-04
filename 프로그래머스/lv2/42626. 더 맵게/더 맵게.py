import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    for val in scoville:
        heapq.heappush(heap,val)
    
    while len(heap) > 1:
        min_val = heapq.heappop(heap)
        if min_val < K :
            second = heapq.heappop(heap)
            heapq.heappush(heap, min_val + second*2)
            answer+=1
        else:
            return answer
    if heap and heap[0] >= K :
        return answer
    else:
        return -1
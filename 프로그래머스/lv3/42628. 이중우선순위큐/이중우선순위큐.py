import heapq
def solution(operations):
    heapMin = []
    heapMax = []
    for operation in operations:
        if operation[0] == "I":
            heapq.heappush(heapMin,int(operation[2:]))
            heapq.heappush(heapMax,-int(operation[2:]))
        elif heapMin:
            if operation[2] == "-":
                temp = heapq.heappop(heapMin)
                heapMax.remove(-temp)
                heapq.heapify(heapMax)
            else:
                temp = heapq.heappop(heapMax)
                heapMin.remove(-temp)
                heapq.heapify(heapMin)
    if heapMin:
        answer = [-heapMax[0],heapMin[0]]
    else: answer = [0,0]
    return answer
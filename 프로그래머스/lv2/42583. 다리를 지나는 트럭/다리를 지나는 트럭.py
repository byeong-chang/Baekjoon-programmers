from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    total = 0
    current = deque([0 for i in range(bridge_length)])
    print(current)
    while current:
        time +=1
        now = current.popleft()
        total -= now
        if truck_weights:
            if total+truck_weights[0] <= weight:
                current.append(truck_weights.pop(0))
                total +=current[-1]
            else: 
                current.append(0)
    return time

solution(	2, 10, [7, 4, 5, 6])
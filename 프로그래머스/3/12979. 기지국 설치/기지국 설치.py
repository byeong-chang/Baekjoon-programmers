import math 

def solution(n, stations, w):
    answer = 0
    current = 1
    length = 2*w +1
    for station in stations:
        start = station - w
        answer += math.ceil((start-current) / length)
        current = start + 2*w+1
    answer += math.ceil((n+1-current) / length)
    return answer
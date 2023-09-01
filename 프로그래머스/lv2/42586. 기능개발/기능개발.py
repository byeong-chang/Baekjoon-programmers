import math #math 모듈을 먼저 import해야 한다.
def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(speeds))]
    currentDay = days[0]
    count = 1
    
    for i in range(1,len(days)):
        if days[i] > currentDay:
            currentDay = days[i]
            answer.append(count)
            count = 1
        else: 
            count+=1
    answer.append(count)
    return answer
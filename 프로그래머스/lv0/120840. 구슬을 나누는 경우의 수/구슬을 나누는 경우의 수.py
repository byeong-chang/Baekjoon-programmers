def solution(balls, share):
    answer = 1
    divide = 1
    for i in range(share):
        answer *= (balls-i) 
        divide *= i+1
    
    return answer / divide
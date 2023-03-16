def solution(numbers, k):
    toss = (k-1) * 2
    answer = numbers[toss % len(numbers)]
    
    return answer
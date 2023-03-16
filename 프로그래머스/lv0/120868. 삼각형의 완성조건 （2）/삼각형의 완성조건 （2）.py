def solution(sides):
    big = max(sides)
    small = min(sides)
    answer = len(range(big-small+1,big+small))
    return answer
45678 
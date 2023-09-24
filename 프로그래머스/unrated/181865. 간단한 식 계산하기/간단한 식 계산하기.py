def solution(binomial):
    answer = binomial.split()
    if answer[1] == '-':
        return int(answer[0]) - int(answer[2])
    elif answer[1] == '+':
        return int(answer[0]) + int(answer[2])
    else: return int(answer[0]) * int(answer[2])
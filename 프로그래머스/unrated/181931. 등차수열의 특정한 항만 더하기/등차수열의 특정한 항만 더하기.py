def solution(a, d, included):
    answer = 0
    for i,flag in enumerate(included):
        if flag : answer = answer+ a+ d*i
    return answer
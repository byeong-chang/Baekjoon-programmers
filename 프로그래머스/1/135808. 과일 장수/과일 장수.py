def solution(k, m, score):
    answer = 0
    length = len(score)
    score.sort(reverse = True)
    for i in range(0,length - length%m,m):
        answer += min(score[i:i+m])*m
    return answer
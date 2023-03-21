def solution(t, p):
    n = len(p)
    answer = 0
    for i in range(len(t)-n+1):
        if int(p) >= int(t[i:i+n]):
            answer +=1
    return answer
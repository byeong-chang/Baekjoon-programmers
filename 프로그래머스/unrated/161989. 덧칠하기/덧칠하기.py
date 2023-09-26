def solution(n, m, section):
    answer,check = 0,0
    while check <= n and section:
        check = section[0] + m
        answer+=1
        while section:
            if section[0] < check:
                section.pop(0)
            else: break
    return answer
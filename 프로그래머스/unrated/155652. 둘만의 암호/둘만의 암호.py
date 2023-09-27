def solution(s, skip, index):
    alpha = [chr(i+97) for i in range(26)]
    for i in skip:
        alpha.remove(i)
    answer = ''
    for i in s:
        answer += alpha[(alpha.index(i) + index)%(len(alpha))]
    return answer
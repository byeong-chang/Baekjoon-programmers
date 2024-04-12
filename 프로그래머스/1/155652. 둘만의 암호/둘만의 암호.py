def solution(s, skip, index):
    alpha = [chr(i+97) for i in range(26)]
    for word in skip:
        alpha.remove(word)
    answer = ''
    for i in s:
        answer += alpha[(alpha.index(i) + index)%(len(alpha))]
    return answer
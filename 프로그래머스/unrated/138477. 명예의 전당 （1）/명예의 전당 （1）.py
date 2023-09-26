def solution(k, score):
    answer = []
    ks = []
    for i in score:
        ks.append(i)
        ks.sort(reverse = True)
        if len(ks) > k:
            ks.pop()
        answer.append(ks[-1])
    return answer
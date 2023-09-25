def solution(arr, k):
    answer = []
    dic = dict()
    for i in arr:
        if i not in dic:
            dic[i] = 0
            answer.append(i)
    if len(answer)< k:
        answer.extend([-1 for _ in range(k-len(answer))])
    return answer[:k]
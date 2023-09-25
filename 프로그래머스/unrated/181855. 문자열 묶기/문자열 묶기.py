def solution(strArr):
    answer = dict()
    for sta in strArr:
        length = len(sta)
        if length in answer:
            answer[length] +=1
        else: answer[length] = 1
    return max(answer.values())
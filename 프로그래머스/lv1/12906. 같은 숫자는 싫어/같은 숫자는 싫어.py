def solution(arr):
    answer=[]
    temp = -1
    for i in arr:
        if i != temp:
            temp = i
            answer.append(i)
    return answer
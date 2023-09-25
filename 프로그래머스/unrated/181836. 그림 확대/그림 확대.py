def solution(picture, k):
    answer=[]
    for pic in picture:
        temp = ''
        for i in pic:
            temp +=i*k
        for i in range(k):
            answer.append(temp)
    return answer
            
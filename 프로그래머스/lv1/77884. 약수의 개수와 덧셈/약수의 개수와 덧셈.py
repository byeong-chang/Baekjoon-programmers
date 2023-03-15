def solution(left, right):
    answer = 0
    for i in range(left, right +1):
        temp = 0
        for j in range(1,i+1):
            if i % j == 0:
                temp+=1
        if temp % 2 == 0:
            answer += i
        else : answer -=i
    return answer
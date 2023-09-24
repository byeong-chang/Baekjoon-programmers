def solution(numLog):
    answer = ''
    for i in range(1,len(numLog)):
        temp = numLog[i] - numLog[i-1]
        if temp == 1:
            answer+='w'
        elif temp == -1:
            answer+='s'
        elif temp == 10:
            answer+= 'd'
        elif temp == -10 : 
            answer +='a'
    return answer
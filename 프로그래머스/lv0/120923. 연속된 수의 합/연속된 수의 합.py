def solution(num, total):
    answer = []
    if num%2 == 0:
        start = total//num-num//2
        for i in range(start+1,start+num+1):
            answer.append(i)
        return answer
    else: 
        start = total//num - num//2
        for i in range(start,start+num):
            answer.append(i)
        return answer
        return answer
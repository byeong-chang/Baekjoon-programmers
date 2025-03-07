answer = []

def solution(n):
    hanoi(n,1,3,2)
    return answer


def hanoi(n,start,end,temp):
    global answer
    if n == 1:
        answer.append([start,end])
        return
    
    hanoi(n-1,start,temp,end)
    answer.append([start,end])
    hanoi(n-1,temp,end,start)
    
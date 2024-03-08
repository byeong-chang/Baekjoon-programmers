def solution(order):
    stack = [-1]
    answer = 0
    length = len(order)
    for i in range(1, length+2):
        while True:
            if length == answer:
                return answer
            
            if stack[-1] == order[answer]:
                stack.pop()
                answer+=1
            else: 
                break
                
        if order[answer] == i:
            answer+=1
        else: 
            stack.append(i)
    return answer
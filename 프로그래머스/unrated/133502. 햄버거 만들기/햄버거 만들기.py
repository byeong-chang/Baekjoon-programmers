from collections import deque

def solution(ingredient):
    ingredient = deque(ingredient)
    stack = []
    answer = 0
    
    while ingredient:
        stack.append(ingredient.popleft())
        if stack[-4:] == [1,2,3,1]:
            for _ in range(4):
                stack.pop()
            answer+=1        
    return answer
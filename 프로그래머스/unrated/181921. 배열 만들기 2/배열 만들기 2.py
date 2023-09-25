def solution(l, r):
    answer = []
    for i in range(l - (l%5),r+1,5):
        if all([ num in ['5','0'] for num in str(i)]):
            answer.append(i)
    if answer:        
        return answer
    else: return [-1]
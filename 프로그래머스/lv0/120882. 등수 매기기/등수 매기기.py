def solution(score):
    score = list(map(sum,score))
    temp = score.copy()
    temp.sort(reverse = True)
    answer = []
    
    for val in score:
        answer.append(temp.index(val)+1)
    
    return answer
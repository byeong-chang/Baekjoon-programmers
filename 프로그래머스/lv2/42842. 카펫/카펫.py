import math
def solution(brown, yellow):
    #brown + yellow의 약수를 찾아서 조건에 맞으면 return
    answers = []
    total = brown+yellow
    for i in range(1,int(math.sqrt(total))+1):
        if total % i == 0:
            answers.append((total//i,i))
    for answer in answers:
        if brown == (answer[0]-1)*2 + (answer[1]-1)*2:
            if yellow == (answer[0]-2)*(answer[1]-2):
                return answer
            
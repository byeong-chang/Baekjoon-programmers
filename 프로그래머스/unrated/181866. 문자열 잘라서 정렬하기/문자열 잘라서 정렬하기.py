def solution(myString):
    answer = []
    for i in sorted(myString.split('x')):
        if len(i) !=0: answer.append(i)
    return answer
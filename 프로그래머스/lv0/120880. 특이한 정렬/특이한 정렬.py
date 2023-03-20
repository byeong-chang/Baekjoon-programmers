import numpy as np
def solution(numlist, n):
    temp = []
    for i in range(len(numlist)):
        temp.append([abs(numlist[i]-n),numlist[i]])
    temp.sort(key = lambda x : (x[0],-x[1]))
    answer = []
    for i in temp:
        answer.append(i[1])
    return answer
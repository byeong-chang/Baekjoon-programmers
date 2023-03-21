from collections import Counter
def solution(array):
    high = 0
    flag = True
    for i,count in Counter(array).items():
        if count > high:
            answer = i
            high = count
            flag = True
        elif count == high:
            flag = False
    if flag:
        return answer
    else: return -1
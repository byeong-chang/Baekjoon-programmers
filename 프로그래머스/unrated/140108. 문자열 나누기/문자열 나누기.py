def solution(s):
    answer = 0
    first,other = [0,0],0
    for i in s:
        if first[1] == 0:
            first[0] = i
            first[1] +=1
        elif i == first[0]:
            first[1] +=1
        else: other +=1
        if first[1] == other:
            answer+=1
            first,other = [0,0],0
    if first[0]: answer+=1
    return answer
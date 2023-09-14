def solution(elements):
    lst = []
    length = len(elements)
    # i = 부분 수열 길이
    for i in range(1,length+1):
        # j = 시작위치
        for j in range(length):
            if j + i > length:
                lst.append(sum(elements[j:]+elements[:j+i-length]))
            else:
                lst.append(sum(elements[j:j+i]))
    answer = list(set(lst))
    return len(answer)
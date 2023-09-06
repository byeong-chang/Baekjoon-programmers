def solution(numbers):
    
    expand = []
    answer = ''
    for number in numbers:
        length = len(str(number))
        expandedNum = str(number)
        while len(expandedNum) <4:
            expandedNum += expandedNum
        expandedNum = expandedNum[:4]
        expand.append([number, int(expandedNum)])
    expand = sorted(expand, key = lambda x : (-x[1],x[0]))
    for num in expand:
        answer += str(num[0])
    return str(int(answer))
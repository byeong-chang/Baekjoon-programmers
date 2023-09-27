def solution(dartResult):
    answer,total = [],[]
    area = ['S','D','T']
    bonus = ['*','#']
    temp = ''
    for dart in dartResult:
        if dart in area:
            answer.append([int(temp),dart])
            temp = ''
        elif dart in bonus:
            answer[-1].append(dart)
        else: temp += dart
    for i in range(0,3):
        if answer[i][1] == 'S':
            total.append(answer[i][0])
        elif answer[i][1] == 'D':
            total.append(answer[i][0]**2)
        elif answer[i][1] == 'T':
            total.append(answer[i][0] **3)
    for i in range(0,3):
        if len(answer[i]) == 3:
            if answer[i][2] == "#":
                total[i] = -total[i]
            else:
                if i >0:
                    total[i] *=2
                    total[i-1] *=2
                else: total[i] *=2
    return sum(total)
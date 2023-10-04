def solution(babbling):
    can = ['aya','ye','woo','ma']
    answer = 0
    for i in range(len(babbling)):
        temp = babbling[i]
        for j in can:
            if j in babbling[i]:
                temp = temp.replace(j,"",1)
        if temp == '':
            answer+=1
            print(i)
    return answer
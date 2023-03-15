def solution(bin1, bin2):
    diff = abs(len(bin1) - len(bin2))
    if len(bin1) > len(bin2):
        bin2 = 0*diff + bin2
    elif len(bin1) < len(bin2):
        bin1 = 0*diff + bin1
    answer = []
    head ,temp= 0,0
    for i in range(len(bin1)-1 , -1 ,-1):
        temp = head + int(bin1[i]) + int(bin2[i])
        if temp == 0:
            answer.append("0")
            head = 0
        elif temp == 2:
            answer.append("0")
            head = 1
        else:
            head = temp//2
            answer.append(str(temp%2))
    if head == 1:
        answer.append(str("1"))
    answer.reverse()
    answer =  "".join(answer)
    return answer
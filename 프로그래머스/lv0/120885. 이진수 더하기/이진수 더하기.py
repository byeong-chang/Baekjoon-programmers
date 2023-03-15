def solution(bin1, bin2):
    temp = 1
    bin_1 = 0
    bin_2 = 0
    answer = []
    for i in range(len(bin1)-1,-1,-1):
        bin_1 += temp*int(bin1[i])
        temp *=2
    temp = 1
    for i in range(len(bin2)-1,-1,-1):
        bin_2 += temp*int(bin2[i])
        temp *=2
    total = bin_1 + bin_2
    print(total)
    while True:
        answer.append(str(total%2))
        total//=2
        if total == 0:
            break
    answer.reverse()
    return "".join(answer)
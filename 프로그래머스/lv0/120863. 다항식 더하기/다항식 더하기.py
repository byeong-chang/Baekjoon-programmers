def solution(polynomial):
    temp = polynomial.split()
    answer = [0,0]
    for word in range(0,len(temp),2):
        if temp[word][-1] == 'x':
            if len(temp[word]) == 1:
                answer[0]+= 1
            else:answer[0] += int(temp[word][:-1])
        else: answer[1] += int(temp[word])
    
    if answer[0] == 0:
        return str(answer[1])
    elif answer[1] == 0:
        if answer[0] == 1:
            return "x"
        else:
            return str(answer[0])+"x"
    else:
        if answer[0] == 1:
            return "x + "+str(answer[1])
        else:
            return str(answer[0]) + "x + "+str(answer[1])
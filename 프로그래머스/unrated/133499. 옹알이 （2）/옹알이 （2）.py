def solution(babbling):
    answer = 0
    canword = ['aya','ye','woo','ma']
    for i in range(len(babbling)):
        temp = [0,0,0,0]
        for j,can in enumerate(canword):
            if can in babbling[i] and can *2 not in babbling[i]:
                babbling[i] = babbling[i].replace(canword[j],' ')
        if len(babbling[i].strip()) == 0:
            answer+=1
    
    return answer
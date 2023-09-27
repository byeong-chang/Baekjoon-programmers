def solution(lottos, win_nums):
    answer = 0
    zero = 0
    for lotto in lottos:
        if lotto in win_nums:
            answer+=1
        if lotto == 0:
            zero+=1
    answer = [answer+zero,answer]
    for i in range(2):
        if answer[i] <2:answer[i] = 6
        else:answer[i] = 7-answer[i]
    return answer
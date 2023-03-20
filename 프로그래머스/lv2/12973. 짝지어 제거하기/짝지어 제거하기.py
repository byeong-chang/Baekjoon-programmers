def solution(s):
    answer = [s[0]]
    for i in range(1,len(s)):
        answer.append(s[i])
        if len(answer)>1:
            if answer[-1] == answer[-2]:
                answer.pop()
                answer.pop()
    if len(answer) == 0: return 1
    else: return 0

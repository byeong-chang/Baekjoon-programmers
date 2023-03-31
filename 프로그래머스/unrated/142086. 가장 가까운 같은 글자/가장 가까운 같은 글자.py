def solution(s):
    answer = []
    for i in range(len(s)):
        val = s[:i][::-1].find(s[i])
        if val == -1:answer.append(val)
        else: answer.append(val+1)
    return answer
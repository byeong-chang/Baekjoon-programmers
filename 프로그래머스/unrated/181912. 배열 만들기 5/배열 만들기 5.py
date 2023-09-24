def solution(intStrs, k, s, l):
    answer = []
    for intstr in intStrs:
        if int(intstr[s: s+l]) >k :
            answer.append(int(intstr[s:s+l]))
    return answer
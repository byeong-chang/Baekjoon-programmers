def solution(s):
    ordinary = []
    for i in s:
        ordinary.append(ord(i))
    answer = ''
    ordinary.sort(reverse = True)
    print(ordinary)
    for i in ordinary:
        answer += chr(i)
    return answer
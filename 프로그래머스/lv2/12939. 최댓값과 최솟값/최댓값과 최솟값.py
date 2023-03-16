def solution(s):
    s = list(map(int,s.split()))
    print(s)
    answer = str(min(s)) + " " + str(max(s))
    return answer
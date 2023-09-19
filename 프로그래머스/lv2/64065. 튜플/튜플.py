def solution(s):
    answer = []
    # 문자열 처리구간
    s = s[1:-2].split("}")
    for i in range(len(s)):
        s[i] = s[i].replace("{","")
        if s[i][0] == ",": s[i] = s[i][1:]
        s[i] = list(map(int,s[i].split(",")))
    # 길이순 정렬
    s.sort(key = lambda x: len(x))
    # 로직수행
    for i in range(len(s)):
        answer.append(s[i][0])
        for j in range(i+1,len(s)):
            s[j].remove(s[i][0])
    return answer
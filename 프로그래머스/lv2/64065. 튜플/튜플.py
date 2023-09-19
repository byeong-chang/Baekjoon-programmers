# 집합을 개수별로 정렬해서 하나씩 answer 배열에 추가하면 되지 않을까 생각함. 
# 근데 그러면 n^2 나올 것으로 예상이 가는데 n이 100000이하니까 이거 시간초과일걸..?

def solution(s):
    answer = []
    # s = s.replace("{","")
    # s = s.replace("}","")
    s = s[1:-2].split("}")
    for i in range(len(s)):
        s[i] = s[i].replace("{","")
        if s[i][0] == ",": s[i] = s[i][1:]
        s[i] = list(map(int,s[i].split(",")))
    s.sort(key = lambda x: len(x))
    for i in range(len(s)):
        answer.append(s[i][0])
        for j in range(i+1,len(s)):
            s[j].remove(s[i][0])
        
    print(s)
    return answer
def solution(lines):
    dic = {i:0 for i in range(-100,101)}
    for line in lines:
        for i in range(line[0],line[1]):
            dic[i]+=1
    answer = 0
    for k,v in dic.items():
        if v > 1:
            answer+=1
            print(k,v)
    return answer
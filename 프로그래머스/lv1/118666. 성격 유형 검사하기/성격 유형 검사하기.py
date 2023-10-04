def solution(survey, choices):
    dic = {'R':0,'T':1,'C':2,'F':3,'J':4,'M':5,'A':6,'N':7}
    point = [0]*8 
    answer = ''
    for i,val in enumerate(survey):
        if choices[i]<4:
            point[dic[val[0]]] += (4-choices[i])
        elif choices[i] > 4:
            point[dic[val[1]]] += (choices[i]-4)
    dic = list(dic.keys())
    for i in range(4):
        if point[2*i] >= point[2*i+1]:
            answer+= dic[2*i]
        else: answer+=dic[2*i+1]
    return answer
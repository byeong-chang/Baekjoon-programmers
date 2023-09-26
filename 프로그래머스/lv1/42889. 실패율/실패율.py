def solution(N, stages):
    answer = []
    dic = {i:0 for i in range(1,N+1)}
    for stage in stages:
        if stage <= N:
            dic[stage] +=1
    count = len(stages)
    for i,v in dic.items():
        temp = dic[i]
        if count:
            dic[i] = temp/count
            count -=temp
    answer = [i[0] for i in sorted(dic.items(), key = lambda x : -x[1])]
    return answer
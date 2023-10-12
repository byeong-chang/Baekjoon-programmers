def solution(n, works):
    '''
    시간 초과가 발생할 것 같은 n 값이다.
    간단하게 생각나는 풀이는 딕셔너리에 모든 works 값 개수를 세서 저장하고,
    n이 0 이 될 때 까지 제일 큰 애들에 대해서만 빼주는 방식을 사용
    '''
    dic = {}
    for work in works:
        if work in dic:
            dic[work] +=1
        else: dic[work] = 1
    big = max(dic.keys())
    while n > 0:
        temp = dic[big]
        if n < temp:
            if (big-1) in dic:
                dic[big-1] +=n
            else: dic[big-1] = n
            dic[big] -=n
        else: 
            if (big-1) in dic:
                dic[big-1] += temp
            else: dic[big-1] = temp
            del dic[big]
            big -=1
        n -= temp
    print(dic)
    answer = 0
    for key,val in dic.items():
        answer += (key**2)*val
    if max(dic.keys()) > 0:
        return answer
    else: return 0
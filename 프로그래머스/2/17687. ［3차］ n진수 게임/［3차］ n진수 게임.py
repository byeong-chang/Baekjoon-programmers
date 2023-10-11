def solution(n, t, m, p):
    # brute force로 풀어보자 : t * m 의 최대 가능 개수가 10만개네 이거 시간복잡도 나쁘면 시간초과 날수도 있겠다
    #걍 해보자 ㄱㄱ
    num = 1
    big = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    brute_force = '0'
    while len(brute_force) < t*m:
        temps,tempn = '',num
        while tempn:
            temps += big[tempn%n]
            tempn //=n
        brute_force += temps[::-1]
        num+=1
    answer = brute_force[p-1::m][:t]
    return answer
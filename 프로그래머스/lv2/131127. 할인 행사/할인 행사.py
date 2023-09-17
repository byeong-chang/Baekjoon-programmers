def check(want, ten):
    flag = 1
    for one in want:
        if one not in ten or ten[one] < want[one]:
            flag = 0
            break
    return flag
# 그러면 discount에 있는 값이 100000 까지 존재할 수 있는데 이걸 10개씩 미루면서 딕셔너리 만들면..
# 
def solution(want, number, discount):
    dic = {}
    want_dic = {}
    answer = 0
    for i in range(10):
        if discount[i] in dic:
            dic[discount[i]] +=1
        else:
            dic[discount[i]] = 1
    for i,val in enumerate(want):
        want_dic[val] = number[i]
    answer += check(want_dic, dic)
    for i in range(10,len(discount)):
        dic[discount[i-10]] -= 1
        if discount[i] in dic:
            dic[discount[i]] +=1
        else:
            dic[discount[i]] = 1
        answer += check(want_dic,dic)
    return answer
def solution(num_list):
    mux = 1
    for i in num_list:
        mux*=i
    if mux >= sum(num_list)**2:
        return 0
    else: return 1
    answer = 0
    return answer
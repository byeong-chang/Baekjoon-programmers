def solution(num_list):
    if len(num_list) >10:
        return sum(num_list)
    else:
        mux = 1
        for i in num_list:
            mux*=i
        return mux
    answer = 0
    return answer
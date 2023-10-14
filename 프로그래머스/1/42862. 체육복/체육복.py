def solution(n, lost, reserve):
    reserve_set = set(reserve)-set(lost)
    lost_set = set(lost) - set(reserve)
    lost = list(lost_set)
    reserve = list(reserve_set)
    answer = n-len(lost)
    lost.sort()
    reserve.sort()
    for value in lost:
        for k in range(-1,2):
            if value+k in reserve:
                reserve.remove(value+k)
                answer+=1
                break
    return answer
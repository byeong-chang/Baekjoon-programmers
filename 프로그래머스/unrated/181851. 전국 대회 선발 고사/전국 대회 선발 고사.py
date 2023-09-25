def solution(rank, attendance):
    lst = sorted([ (v,i) for i,v in enumerate(rank) if attendance[i]])
    return 10000 * lst[0][1] + 100 * lst[1][1] + lst[2][1]

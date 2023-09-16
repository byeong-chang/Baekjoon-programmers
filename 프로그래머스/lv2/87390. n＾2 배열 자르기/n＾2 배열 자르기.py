import itertools
def solution(n, left, right):
    temp = []
    lst = [i for i in range(1,n+1)]
    for i in range(left//n + 1,right//n +2):
        temp.append([i for j in range(i)]+lst[i:])
    temp[-1] = temp[-1][:right%n+1]
    answer =list(itertools.chain(*temp))[left%n:]
    return answer
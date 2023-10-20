def solution(m, n, puddles):
    lst=[[0]*(m+1) for _ in range(n+1)]
    lst[0][1] = 1
    for puddle in puddles:
        lst[puddle[1]][puddle[0]] = -1
    for i in range(1,len(lst)):
        for j in range(1,len(lst[0])):
            if lst[i][j] == -1:
                continue
            up,left = lst[i-1][j],lst[i][j-1]
            if up == -1: up = 0
            if left == -1 : left = 0
            lst[i][j] = (up+left)%1000000007
    return lst[-1][-1]
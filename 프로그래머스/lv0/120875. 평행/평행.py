def solution(dots):
    for i in range(1,len(dots)):
        lst = [1,2,3]
        lst.remove(i)
        axis1 = (max(dots[i][0] , dots[0][0]) - min(dots[i][0] , dots[0][0]))/ (max((dots[i][1] , dots[0][1]))-min((dots[i][1] , dots[0][1])))
        axis2 = (dots[lst[0]][0] - dots[lst[1]][0])/(dots[lst[0]][1] - dots[lst[1]][1])
        if axis1 == axis2 :
            return 1    
    return 0
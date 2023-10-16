def solution(park, routes):
    current,x,y = 0,len(park[0]),len(park)
    for j in range(y):
        for i in range(x):
            if park[j][i] == 'S':
                current = [j,i]
    for route in routes:
        dt,ds = route[0], int(route[2:])
        direction = [0,0]
        if dt =='E':direction = [0,1]
        elif dt =='W' : direction = [0,-1]
        elif dt == 'N' : direction =[-1,0]
        elif dt == 'S' : direction = [1,0]
        dy,dx = current[0] + ds*direction[0], current[1] + ds*direction[1]
        if  dy>= y or dy <0 or dx>=x or  dx< 0:
            continue
        for i in range(1,ds+1):
            if park[current[0] + i*direction[0]][current[1] + i*direction[1]] =='X':
                break
        else: 
            current = [current[0]+direction[0]*ds,current[1]+direction[1]*ds]
            print(current)
    return current
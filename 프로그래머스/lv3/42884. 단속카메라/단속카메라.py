def solution(routes):
    answer = 0
    camera = -30001
    sortedRoutes = sorted(routes, key = lambda x : (x[1],x[0]))
    for route in sortedRoutes:
        if route[0] > camera:
            answer +=1
            camera = route[1]
    return answer
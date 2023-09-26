def solution(a, b, c, d):
    lst = [a,b,c,d]
    lst.sort()
    if lst[0] == lst[3]:
        return 1111* a
    elif lst[0] == lst[2]:
        return (10*lst[0] + lst[3])**2
    elif lst[1] == lst[3]:
        return (10*lst[3] + lst[0])**2
    elif lst[0] == lst[1] and lst[2] == lst[3]:
        return (lst[0] + lst[2]) * abs(lst[0] - lst[2])
    elif lst[0] == lst[1]:
        return lst[2] * lst[3]
    elif lst[1] == lst[2]:
        return lst[0] * lst[3]
    elif lst[2] == lst[3]:
        return lst[0] * lst[1]
    else: return min(lst)
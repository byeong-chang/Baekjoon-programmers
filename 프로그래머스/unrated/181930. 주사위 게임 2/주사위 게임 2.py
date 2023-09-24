def solution(a, b, c):
    if a == b and b == c:
        return (a+b+c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif a==b or b==c or a == c:
        return (a+b+c) * (a**2 + b**2 + c**2)
    else: return (a+b+c)
    answer = 0
    return answer
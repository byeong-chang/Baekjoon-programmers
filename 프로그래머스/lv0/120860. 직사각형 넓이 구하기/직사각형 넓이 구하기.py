def solution(dots):
    dots.sort()
    print(dots)
    y = abs(dots[0][1] - dots[1][1])
    x = abs(dots[0][0] - dots[3][0])
    answer = x*y
    return answer
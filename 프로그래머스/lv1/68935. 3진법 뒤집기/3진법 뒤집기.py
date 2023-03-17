def solution(n):
    answer = []
    while n != 0:
        answer.append(n%3)
        n //= 3
    answer.reverse()
    count = 1
    sol = 0
    for i in range(len(answer)):
        sol += answer[i]*3**i
    return sol
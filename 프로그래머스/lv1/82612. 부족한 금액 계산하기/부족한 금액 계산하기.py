def solution(price, money, count):
    answer = 0
    mux = 1
    for i in range(count):
        answer += mux*price
        mux +=1
    if answer > money:
        return answer-money
    else: return 0
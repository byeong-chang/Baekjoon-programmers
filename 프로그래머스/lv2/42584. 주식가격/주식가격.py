def solution(prices):
    
    answer = [0 for _ in range(len(prices))]
    temp = []
    for i in range(len(prices)-1):
        temp.append([prices[i],i])
        while temp and temp[-1][0] > prices[i+1]: 
            val, time = temp.pop()
            answer[time] = i-time +1
    for t in temp:
        answer[t[1]] = len(prices) - t[1]-1
    return answer
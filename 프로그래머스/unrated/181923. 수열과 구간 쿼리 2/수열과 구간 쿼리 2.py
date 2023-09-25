def solution(arr, queries):
    answer = []
    for query in queries:
        temp = []
        s,e,k = query
        for i in arr[s:e+1]:
            if i > k:
                temp.append(i)
        if temp:
            answer.append(min(temp))
        else: answer.append(-1)
            
    return answer
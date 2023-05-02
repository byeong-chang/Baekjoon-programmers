def solution(arr, k):
    if k%2 == 0:
        answer = [i+k for i in arr]
    else: answer = [i*k for i in arr]
        
    return answer
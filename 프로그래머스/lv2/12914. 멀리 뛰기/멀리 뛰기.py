def solution(n):
    arr = [0]*2023
    arr[1] = 1
    arr[2] = 2
    for i in range(3,n+1):
        arr[i] = arr[i-1] + arr[i-2]
    
    return arr[n]%1234567
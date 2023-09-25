def solution(arr):
    length = len(arr)
    n = 1
    while length > n:
        n*=2
    for i in range(n-length):
        arr.append(0)
    return arr
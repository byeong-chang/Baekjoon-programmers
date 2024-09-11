def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
                
def solution(arr):
    answer = arr[-1]
    for i in range(len(arr)-1):
        big,small = max(answer,arr[i]),min(answer,arr[i])
        answer = abs(big*small) // gcd(small,big)
    return answer
def solution(array, n):
    answer = 0
    temp = 300
    array.sort(reverse = True)
    for i in array:
        if temp >= abs(n-i):
            temp = abs(n-i)
            answer = i
    return answer
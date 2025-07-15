def solution(numbers, n):
    total = 0
    for num in numbers:
        total+= num
        if total > n:
            break
    
    
    return total
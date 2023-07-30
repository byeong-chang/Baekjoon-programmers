def solution(numbers, target):
    check = [0]
    for num in numbers:
        for i in range(len(check)):
            check.append(check[i]-num)
            check[i] = check[i] + num
    answer = check.count(target)
    return answer

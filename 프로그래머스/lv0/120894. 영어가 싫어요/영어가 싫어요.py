def solution(numbers):
    answer = ""
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    temp = ""
    for i in numbers :
        temp += i
        if temp in nums:
            answer += str(nums.index(temp))
            temp = ""
            
    return int(answer)
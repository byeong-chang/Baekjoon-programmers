import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
nums = list(map(int,input().split()))
cost = int(input())

left = cost//N - 1
right = max(nums)
answer = -1

while left <= right:
    middle = (left+ right)//2
    
    total = 0
    for num in nums:
        if num > middle:
            total += middle
        else: 
            total += num
    
    if total > cost: 
        right = middle - 1
    else: 
        left = middle + 1
        answer = middle
print(answer)
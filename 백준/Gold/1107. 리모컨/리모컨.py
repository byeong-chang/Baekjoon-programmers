import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
broken = list(sys.stdin.readline().split())

min_num = abs(100-N)

for nums in range(1000001):
    nums = str(nums)
    for j in range(len(nums)):
        if nums[j] in broken:
            break
        elif j == len(nums)-1:
            min_num = min(min_num,len(nums)+abs(int(nums)-N))
print(min_num)
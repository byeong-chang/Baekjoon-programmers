import sys

N,M = map(int,sys.stdin.readline().rstrip().split(" "))
nums = list(map(int,sys.stdin.readline().rstrip().split(" ")))

maxVal = -1
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            temp = nums[i] + nums[j] + nums[k]
            if temp > maxVal and temp <= M:
                maxVal = temp

print(maxVal)

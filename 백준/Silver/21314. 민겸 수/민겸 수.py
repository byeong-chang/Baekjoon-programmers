import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

nums = input()
min, max = "", []

#max
kCount = 0
for i in range(len(nums)-1,-1,-1):
    if nums[i] == "K":
        if kCount:
            max.append("5" + "0"*(kCount-1))
        kCount = 1
            
    else:
        if kCount:
            kCount+=1
        else:
            max.append("1")
if kCount:
    max.append("5" + "0"*(kCount-1))
    kCount = 0
print(int("".join(max[::-1])))

#min
mCount = 0
for num in nums:
    if num == "M":
        mCount +=1
    else:
        if mCount:
            min += ("1" + "0" * (mCount-1))
            mCount = 0
        min += "5"
if mCount:
    min += ("1" + "0" * (mCount-1))
print(int(min))

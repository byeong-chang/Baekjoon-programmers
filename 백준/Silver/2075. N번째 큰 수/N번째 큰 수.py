import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

nums = []

def binary_search(v):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < v:
            left = mid + 1
        else:
            right = mid - 1
    return left

def sorting(v):
    global nums
    pos = binary_search(v)
    nums.insert(pos, v)

    if len(nums) > N:
        nums.pop(0)

for _ in range(N):
    for val in list(map(int, input().split())):
        sorting(val)

print(nums[0])

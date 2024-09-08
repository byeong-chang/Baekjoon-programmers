import sys
N = int(sys.stdin.readline().rstrip())
nums = sys.stdin.readline().rstrip()
print(sum([int(nums[i]) for i in range(N)]))
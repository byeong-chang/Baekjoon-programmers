import sys

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    nums = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    print(min(nums), max(nums))

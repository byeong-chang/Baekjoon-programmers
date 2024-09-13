import sys

N = int(sys.stdin.readline().rstrip())

arr = set()
for _ in range(N):
    arr.add(sys.stdin.readline().rstrip())

print(*sorted(arr, key = lambda x : (len(x), x)),sep = "\n")
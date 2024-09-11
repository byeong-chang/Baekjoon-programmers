import sys

N = int(sys.stdin.readline().rstrip())
lst = [0,1]

for i in range(2,N+1):
    lst.append(lst[i-1] + lst[i-2])
print(lst[N])
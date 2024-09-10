import sys

T = int(sys.stdin.readline().rstrip())
lst = [0,1]
for i in range(2,T+1):
    lst.append(lst[-1] + lst[-2])
print(lst[T])
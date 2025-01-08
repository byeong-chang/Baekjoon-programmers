import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
lst = sorted(list(map(int,input().split())))
last = 0
if N %2 == 1:
    last = lst.pop()

temp = [lst[i] + lst[-i-1] for i in range(N//2)]
temp.append(last)

print(max(temp))
import sys

def input():
    return sys.stdin.readline().rstrip()

input()
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.extend(b)
a.sort()
print(*a)
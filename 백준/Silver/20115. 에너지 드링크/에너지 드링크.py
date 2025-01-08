import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

lst = list(map(int,input().split()))

maximum = max(lst)
total = sum(lst) - maximum

print(maximum + round(total/2,2))
import sys

def input():
    return sys.stdin.readline().rstrip()

S = int(input())
total = 0
for i in range(1,S+1):
    total += i
    if total > S:
        break

if i == 1: print(i)
else:print(i-1)


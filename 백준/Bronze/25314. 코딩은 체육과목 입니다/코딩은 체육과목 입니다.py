import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
for i in range(n//4):
    print("long",end = " ")
print("int")
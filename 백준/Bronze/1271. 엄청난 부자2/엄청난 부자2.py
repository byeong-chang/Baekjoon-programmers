import sys

def input():
    return sys.stdin.readline()

a,b = map(int,input().split())

print(a//b)
print(a%b)
import sys

def input():
    return sys.stdin.readline().rstrip()


n = int(input())
if n == 1 or n == 3:
    print(-1)
else:
    if (n % 5) % 2 == 0:
        print(n//5 + (n % 5)//2)
    else:
        print(n//5 - 1 + (n % 5 + 5)//2)
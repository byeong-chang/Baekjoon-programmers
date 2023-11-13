import sys
global a, c

def check(n):
    global a, c
    if n == 1:
        return a%c 
    temp = check(n//2) % c
    if n %2 == 0:
        return temp*temp % c
    else: return a*temp*temp %c

a,b,c = map(int,sys.stdin.readline().split())

answer = check(b)
print(answer)
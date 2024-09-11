import sys
A,B,C,M = map(int,sys.stdin.readline().rstrip().split())
man,work = 0,0

for _ in range(24):
    if man + A <= M :
        man +=A
        work += B
    else:
        man -= C
        if man < 0 : man = 0
    
print(work)

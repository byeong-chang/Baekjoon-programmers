
import sys
N,M = map(int,sys.stdin.readline().split())
not_hear = set()
not_see = set()
for i in range(N):
    not_hear.add(sys.stdin.readline())
for j in range(M):
    not_see.add(sys.stdin.readline())
lst = sorted(list(not_hear & not_see))
print(len(lst))
for i in lst:
    print(i,end = "")
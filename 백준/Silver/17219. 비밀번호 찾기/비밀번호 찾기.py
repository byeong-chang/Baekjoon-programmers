import sys
n,m = map(int,sys.stdin.readline().split())
domainPW = {}
for i in range(n):
    domain,pw = sys.stdin.readline().split()
    domainPW[domain] = pw
for i in range(m):
    find = sys.stdin.readline().strip()
    print(domainPW[find])
import sys

def input():
    return sys.stdin.readline().rstrip()

n,k = map(int, input().split())
ns = [i for i in range(1,n+1)]

answer = []
cur = 0

for i in range(n):
    cur += k-1  
    if cur >= len(ns):  
        cur = cur%len(ns)
    answer.append(str(ns.pop(cur)))

print("<",end= "")
for j in range(len(answer)):
    if j == len(answer) -1:
        print(answer[j],end = ">\n")
    else:
        print(answer[j], end = ", ")

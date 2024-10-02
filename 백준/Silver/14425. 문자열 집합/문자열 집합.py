
import sys

def input():
    return sys.stdin.readline().rstrip()

n,m = map(int, input().split())
count = 0 
dic = dict()

for _ in range(n):
    dic[input()] = ''
for _ in range(m):
    if input() in dic:
        count+=1
print(count)

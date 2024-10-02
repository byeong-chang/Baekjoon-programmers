
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
lst = []

for _ in range(n):
    lst.append(int(input()))

lst.sort(reverse = True)
answer = 0
for i in range(0,n,3):
    answer += sum(lst[i:i+3][:2])
print(answer)
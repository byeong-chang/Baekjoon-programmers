import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
lst = []

for _ in range(N):
    lst.append(int(input()))
lst.sort(reverse = True)

tip = 0
for i,v in enumerate(lst):
    temp = v -i
    if temp > 0:
        tip +=temp
print(tip)
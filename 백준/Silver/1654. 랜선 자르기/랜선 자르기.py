import sys
def input():
    return sys.stdin.readline().rstrip()

K,N = map(int,input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))
left,right = 1,max(lines)

while left <= right:
    middle = (left + right) //2
    count = 0
    for line in lines:
        count += line // middle
    if count >= N:left = middle+1
    else: right = middle-1
print(right)

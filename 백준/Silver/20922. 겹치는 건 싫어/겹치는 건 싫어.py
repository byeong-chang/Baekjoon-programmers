import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

n,k = map(int,input().split())
lst = list(map(int,input().split()))
maxLength = 0
ans = {}
count = 0
startIndex = 0
lastIndex = 0

while lastIndex < n:
    if lst[lastIndex] in ans:
        if ans[lst[lastIndex]] >= k:
            maxLength = max(maxLength,count)
            ans[lst[startIndex]]-=1
            startIndex += 1
            count-=1
        else:
            ans[lst[lastIndex]] += 1
            lastIndex +=1
            count+=1
    else:
        ans[lst[lastIndex]] = 1
        lastIndex +=1
        count+=1

print(max(maxLength,count))

import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

n = int(input())

lst = list(map(int,input().split()))
remove = int(input())
linkedDict = {i : [] for i in range(n)}

for j,num in enumerate(lst):
    if num == -1:
        continue
    else:
        linkedDict[num].append(j)

queue = deque([remove])

if lst[remove] != -1:
    linkedDict[lst[remove]].remove(remove)

while queue:
    current = queue.popleft()
    for val in linkedDict[current]:
        queue.append(val)

    linkedDict.pop(current)

answer=0
for val in linkedDict.values():
    if not val:
        answer+=1

# print(linkedDict)

print(answer)
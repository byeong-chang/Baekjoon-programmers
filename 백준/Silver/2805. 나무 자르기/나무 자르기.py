import sys
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int,input().split())
trees = list(map(int,input().split()))

left,right = 0,max(trees)

while left <= right:
    middle = (left+right) //2

    total = 0
    for tree in trees:
        if middle < tree:
            total += tree-middle
        if total > M:
            break
    if total >= M:
        left = middle + 1
    else:
        right = middle - 1

print(right)
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
# map(int,input().split())

n = int(input())
# 모두 root부터 시작
root = "A"
trees = {}
for _ in range(n):
    a,b,c = input().split()
    trees[a] = [b,c]

# 전위 순회
def front(root):

    print(root,end = "")
    left,right = trees[root]
    if left != ".":
        front(left)

    if right != ".":
        front(right)
        
front(root)
print()

# 중위 순회
# 단순 재귀로 풀었음 끝날때 자기자신 출력하도록 설정
# 값을 넣을때 오른쪽 -> 왼쪽 순서로 넣어줘야함.
def middle(root):

    left,right = trees[root]
    if left != ".":
        middle(left)
    print(root,end = "")

    if right != ".":
        middle(right)

middle(root)
print()


# 후위 순회
# dfs로 만들고, 먼저 도착한 값을 나중에 출력하면 됨
# 값 넣을때 왼쪽 -> 오른쪽으로 넣어서 오른쪽이 뒤에 출력하도록 유도
def dfs(stack):
    if not stack:
        return
    current = stack.pop()
    left,right = trees[current]
    if left != ".":
        stack.append(left)
    if right != ".":
        stack.append(right)
    dfs(stack)
    print(current,end = "")

stack = [root]
dfs(stack)
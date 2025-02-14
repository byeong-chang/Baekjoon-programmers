
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
    
n = int(input())
costs = [list(map(int,input().split())) for _ in range(n)]
answer = 200 * 5 * 3 # 최댓값
dx = [0,1,-1,0,0]
dy = [0,0,0,1,-1]

def checkSeed(visited, i,j):
    total = 0
    lst = []
    for k in range(5):
        dxi = i + dx[k]
        dyi = j + dy[k]
        if [dxi,dyi] in visited:
            return False
        else: 
            total += costs[dxi][dyi]
            lst.append([dxi,dyi])

    return total, lst

def dfs(visited,cost):
    global answer
    if cost >= answer:
        return
    if len(visited) >= 15:
        answer = min(answer,cost)
        return
        
    for i in range(1,n-1):
        for j in range(1,n-1):
            temp = checkSeed(visited,i,j)
            if temp:
                flowerCost,flowerVisited = temp
                dfs(visited + flowerVisited,cost + flowerCost)
    
dfs([],0)

print(answer)

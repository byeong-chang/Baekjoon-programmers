
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
dx = [0,0,1,1]
dy = [0,1,0,1]
while len(lst) != 1:
    length = len(lst)//2
    temp = []
    for i in range(length):
        row = []
        for j in range(length):
            row.append(sorted([lst[2*i+dx[k]][2*j +dy[k]] for k in range(4) ])[2])
            
        temp.append(row)
    
    lst = temp[::]

print(lst[0][0])
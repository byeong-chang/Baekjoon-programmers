import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
mines = [input() for _ in range(n)]
opens = [input() for _ in range(n)]
dx = [-1, -1, -1, 0, 0 ,1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
answer = []
flag = False

for i,open in enumerate(opens):
    temp = []
    for j,val in enumerate(open):
        if val == ".":
            temp.append(".")
        else:
            counting = 0
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]
                if -1 < x < n and -1 < y < n:
                    if mines[x][y] == "*":
                        counting+=1
            temp.append(str(counting))

            if mines[i][j] == "*":
                flag = True
            
    answer.append(temp)

if flag:
    for i in range(n):
        for j in range(n):
            if mines[i][j]=='*':
                answer[i][j] = '*'

for a in answer:
    print(*a, sep = "")

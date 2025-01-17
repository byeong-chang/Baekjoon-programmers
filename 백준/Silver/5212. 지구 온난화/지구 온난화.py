
import sys
def input():
    return sys.stdin.readline().rstrip()

R,C = map(int,input().split())

arr = [list(input()) for _ in range(R)]
after50 = [['.']* C  for _ in range(R)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
minX,minY,maxX,maxY = 10,10,0,0

# X 면 4면 검색 후 3개 이상이 바다일 경우 . 으로 바꿔줌
for i in range(R):
    for j in range(C):
        if arr[i][j] == "X":
            count = 0
            for k in range(4):
                tx, ty = j + dx[k],i + dy[k]
                if tx > -1 and ty > -1 and tx < C and ty < R:
                    if arr[ty][tx] == ".":
                        count +=1
                else: count +=1
            
            if count < 3:
                after50[i][j] = 'X'
                if i < minY : minY = i
                if i > maxY : maxY = i

                if j < minX : minX = j
                if j > maxX : maxX = j

# X의 x값 최소 최대, X의 y값 최소 최대를 구해 지도를 그림.
for i in range(minY,maxY+1):
    for j in range(minX,maxX+1):
        print(after50[i][j],end = "")
    print()
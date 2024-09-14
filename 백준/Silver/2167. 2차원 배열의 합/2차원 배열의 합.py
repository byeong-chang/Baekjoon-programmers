import sys

def input():
    return sys.stdin.readline().rstrip()

N,M = map(int, input().split(' '))
lst = []
for _ in range(N):
    lst.append(list(map(int,input().split(" "))))

K = int(input())
for _ in range(K):
    i,j,x,y = map(int, input().split(" "))
    i,j,x,y  = i-1,j-1,x-1,y-1 
    total = 0
    for line in range(i,x+1):
        total += sum(lst[line][j:y+1])
    print(total)
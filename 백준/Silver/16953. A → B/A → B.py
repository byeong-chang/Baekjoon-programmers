
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

a,b = map(int,input().split())

def bfs(val,count):
    if val > b:
        return
    if val == b :
        print(count)
        exit()

    bfs(val*2,count+1)
    bfs(val*10 + 1 , count+1)
bfs(a,1)
print(-1)
import sys

def input():
    return sys.stdin.readline().rstrip()


A = int(input())
T = int(input())
W = int(input())
lst = [0,1,0,1,0,0,1,1]
temp = 0
index = 0 
while True:
    if len(lst) == index:
        lst.insert(4,0)
        lst.insert(-1,1)
        temp += index
        index = 0
    
    if lst[index] == W:
        T-=1
    
    if T == 0:
        print((temp + index) % A)
        break

    index +=1

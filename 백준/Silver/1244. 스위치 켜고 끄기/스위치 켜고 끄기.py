import sys

def input():
    return sys.stdin.readline().rstrip()

input()

lst = list(map(int,input().split()))
lst.insert(0,-1)
n = int(input())

for _ in range(n):
    sex, num = map(int,input().split())
    if sex == 1:
        for i in range(num,len(lst),num):
            lst[i] = (lst[i]+1) % 2
    else:
        lst[num] = (lst[num]+1) % 2
        for j in range(1, min(num, len(lst) - num)):
            if lst[num - j] == lst[num + j]:
                lst[num-j] = (lst[num-j]+1) % 2
                lst[num+j] = (lst[num+j]+1) % 2
            else: break
for i in range(1,len(lst)):
    print(lst[i], end = " ")
    if i % 20 == 0 :
        print()
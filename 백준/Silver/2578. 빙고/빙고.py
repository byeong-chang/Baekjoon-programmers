import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

'''시간복잡도는 고려하지 않아도 되는 구현문재로 보였다.'''
lst = []
check = [0]*25
orders = []
for _ in range(5):
    lst.extend(list(map(int,input().split())))

for _ in range(5):
    orders.extend(list(map(int,input().split())))

count = 0
for i,val in enumerate(orders):
    if count >= 3:
        print(i)
        break

    term = lst.index(val)
    check[term] = 1
    x,y = term%5, term//5

    # 역대각선 체크
    if x == y:
        for j in range(5):
            if check[5 * j + j] != 1:
                break
        else:
            count+=1
    # 역대각선 체크
    if x + y == 4:
        for j in range(5):
            if check[5 * j + 4 - j] != 1:
                break
        else:
            count+=1
    # 가로 체크
    for j in range(5):
        if check[5*y +j] !=1:
            break
    else: count+=1
    # 세로 체크
    for j in range(5):
        if check[x + j*5] !=1:
            break
    else: count+=1



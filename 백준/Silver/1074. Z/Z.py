import sys
N,r,c = map(int,input().split())
# 재귀를 사용한 Divde and conquer로 풀어보자

def func_z(num,row,colum):

    if num ==0 :
        return 0
    elif row < 2**(num-1) and colum < 2**(num-1):
        return func_z(num-1,row%(2**(num-1)),colum%(2**(num-1)))
    elif row >= 2**(num-1) and colum < 2**(num-1):
        return func_z(num-1,row%(2**(num-1)),colum%(2**(num-1))) + 2*2**(2*num-2)
    elif row < 2**(num-1) and colum >= 2**(num-1):
        return func_z(num-1,row%(2**(num-1)),colum%(2**(num-1))) + 2**(2*num-2)
    elif row >= 2**(num-1) and colum >= 2**(num-1):
        return func_z(num-1,row%(2**(num-1)),colum%(2**(num-1))) + 3*2**(2*num-2)

print(func_z(N,r,c))
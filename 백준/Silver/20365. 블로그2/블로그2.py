'''
변경될 때 마다 딕셔너리에 R, B의 개수를 증가시켜주고,
더 적은 값을 기준으로 +1(반대색으로 다 칠하기) 하면 되는 Greedy 문제
'''
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
color = input()

check = {"R" : 0 , "B" : 0}

temp = color[0]
if temp == "R": check['R'] +=1
else: check['B'] +=1

for i in range(1,len(color)):
    if color[i] != temp:
        temp = color[i]
        check[temp] +=1
        
print(min(check.values())+1)
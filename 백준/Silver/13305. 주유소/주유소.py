'''
데이터 10만개 기준 -> nlogn 이하로 코드 작성
'''

def input():
    return sys.stdin.readline()
import sys

N = int(input())
length = list(map(int,input().split()))
cost = list(map(int,input().split()))

total, minmum = 0,cost[0]

for i in range(len(length)):

    if minmum > cost[i]:
        minmum = cost[i]

    total += minmum * length[i]

print(total)
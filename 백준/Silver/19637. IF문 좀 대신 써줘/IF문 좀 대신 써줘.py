'''
단순히 순서대로 구현하기엔  칭호가 100000까지 존재하며 데이터의 개수도 100000임.
N^2로는 풀 수 없음
'''
import sys

def input():
    return sys.stdin.readline().rstrip()


N,M = map(int,input().split())
titles = [['temp',-1]]
for _ in range(N):
    name,score = input().split()
    if int(score) > titles[-1][1]:
        titles.append([name,int(score)])
titles.pop(0)
users = [int(input()) for _ in range(M)]

for user in users:
    left,right = 0, len(titles)-1
    while True:
        middle = (left+right)//2
        if user <= titles[middle][1]:
            right = middle -1
        else:
            left = middle + 1
        if left > right:
            print(titles[left][0])
            break
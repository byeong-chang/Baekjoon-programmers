
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

check = [str(i) for i in range(10)]
translated = [[],[]]
maxVal = 2**63

words = input().split()
for i,word in enumerate(words):
    # 진법 변환을 위한 최소단위를 구한다.
    temp = max(word)
    check_start = 2
    
    # 0~9의 숫자라면 47을 빼주고, 문자라면 86을 빼준다.
    if temp in check: check_start = max(ord(temp) - 47,check_start)
    else: check_start = ord(temp) - 86

    # 가능한 최소 진볍 변환부터 36진법까지 변환해서 저장한다.
    for j in range(check_start,37):
        changed = int(word,j)
        if changed < maxVal:
            translated[i].append([changed,j])

# 변환한 int값이 같은 경우를 뽑는다.
answer = []
for i in range(len(translated[0])):
    for j in range(len(translated[1])):
        # x값이 같고, a,b가 다른 경우엔 정답에 추가
        if translated[0][i][0] == translated[1][j][0] and translated[0][i][1] != translated[1][j][1]:
            answer.append([translated[0][i][0],translated[0][i][1],translated[1][j][1]])

if len(answer) == 0:
    print("Impossible")
elif len(answer) > 1 :
    print("Multiple")
else: print(answer[0][0],answer[0][1],answer[0][2])


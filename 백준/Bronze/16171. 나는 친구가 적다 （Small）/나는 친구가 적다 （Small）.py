# '''
# 숫자 제거 후 연속성 확인
# '''
import sys

text = sys.stdin.readline().rstrip()
temp = ""
answer = sys.stdin.readline().rstrip()
length = len(answer)

for t in text:
    if not (ord(t) > 47 and ord(t) < 58):
        temp += t

for i in range(0,len(temp) - length+1):
    if temp[i] == answer[0]:
        if temp[i:length+i] == answer:
            print(1)
            break
else: print(0)
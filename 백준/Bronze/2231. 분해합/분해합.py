import sys

T = sys.stdin.readline().rstrip()
checkLength = int(T)-len(T)*9-1
if checkLength < 0 : checkLength = 0
T = int(T)
answer = []

for i in range(T-1,checkLength,-1):
    temp = i
    for val in str(i):
        temp += int(val)
    if temp == T:
        answer.append(i)

if answer:    print(answer[-1])
else:   print(0)

import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
answer = {}
for _ in range(N):
    expander = input().split(".")[1]
    if answer.get(expander): answer[expander] +=1
    else: answer[expander] = 1
answer = sorted(answer.items(),key = lambda x:x[0])
for key,val in answer:
    print(key,val)
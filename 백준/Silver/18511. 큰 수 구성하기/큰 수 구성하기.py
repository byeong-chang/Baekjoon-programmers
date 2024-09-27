import sys

def input():
    return sys.stdin.readline().rstrip()

num, k = map(int,input().split())
lst = list(input().split())
lst.sort(reverse = True)
length = len(str(num))
sel = [0] * length
answer = []

def perm(depth):
    if depth == length:
        return int("".join(sel))
    for i in range(len(lst)):
        sel[depth] = lst[i]
        result = perm(depth+1)
        if result and result <= num:
            answer.append(result)
            break

perm(0)
if answer:
    print(answer[0])
else: # 조건에 맞는게 없으면 자릿수 낮춰서 가장 큰 값 출력
    print(int(lst[0] * (length-1)))
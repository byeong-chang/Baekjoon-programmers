import sys

T = sys.stdin.readline().rstrip().split(".")
answer = []

for text in T:
    if text == ".":
        answer.append(".")
        continue
    if len(text) % 4 == 0:
        answer.append("AAAA"*(len(text)//4))
    elif len(text) % 2 == 0:
        answer.append("AAAA" * (len(text)//4) + "BB" * ((len(text)%4)//2))
    else:
        print(-1)
        break
    answer.append(".")
else:
    for a in answer[:-1]:
        print(a,end = "")
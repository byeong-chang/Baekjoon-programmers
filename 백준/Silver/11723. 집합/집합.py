import sys
n = int(sys.stdin.readline())
empty = [0 for i in range(20)]
all =[1 for i in range(20)]
S =[0 for i in range(20)]
for i in range(n):
    text = sys.stdin.readline().split()
    if text[0] =="check":
        print(S[int(text[1])-1])
    elif text[0] == "remove":
        S[int(text[1])-1] = 0
    elif text[0] == "add":
        S[int(text[1])-1] = 1
    elif text[0] == "toggle":
        if S[int(text[1])-1]==0: S[int(text[1])-1]=1
        else: S[int(text[1])-1]=0
    elif text[0] =="all":
        S = all
    elif text[0] =="empty":
        S = empty
import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline()
Pn = 'I'+'OI' *N
str_len = len(Pn)
S_len = len(S)
count=0
for i in range(S_len):
    if S[i] =='I'and S_len - i >= str_len:
        if S[i:i+str_len] == Pn:
            count+=1
print(count)
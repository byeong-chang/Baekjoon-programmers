import sys

def input():
    return sys.stdin.readline().rstrip()

N,K = map(int,input().split())
s = list(map(int,input().split()))
d = list(map(int,input().split()))

'''d에 있는 순서대로 d에있는 값으로 보내면 됨'''


for _ in range(K):
    temp = [0 for _ in range(N+1)]
    for i,index in enumerate(d):
        temp[index] = s[i]
    s = temp[1:]
print(*s)
import sys

N = int(sys.stdin.readline().rstrip())

direction,count = {},0
for _ in range(N):
    cow,dic = map(int, sys.stdin.readline().rstrip().split(" "))
    if cow in direction and direction[cow] != dic:
        count +=1
    direction[cow] = dic
print(count)
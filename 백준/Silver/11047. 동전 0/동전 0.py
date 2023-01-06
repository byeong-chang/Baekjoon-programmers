import sys
N,K = map(int,sys.stdin.readline().split())
coins =[]
count =0
for i in range(N):
    coins.append(int(sys.stdin.readline()))
coins.reverse()
for _ in coins:
    count += K//_
    K %= _
print(count)
import sys
N,M = map(int,sys.stdin.readline().split())
value_lst = list(map(int,sys.stdin.readline().split()))
cummulate_sum = [0]

temp =0
for i in value_lst:
    temp +=i
    cummulate_sum.append(temp)

for _ in range(M):
    i,j = map(int,sys.stdin.readline().split())
    print(cummulate_sum[j]-cummulate_sum[i-1])

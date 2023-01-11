import sys
n = int(sys.stdin.readline())
DP =[0,1,3]
for i in range(3,n+1):
    if i%2 == 0:
        DP.append(DP[i-1]*2+1)
    else: 
        DP.append(DP[i-1]*2-1)
print(DP[n]%10007)
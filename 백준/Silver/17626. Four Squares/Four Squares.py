import sys
n = int(sys.stdin.readline())
DP = [0,1]
for i in range(2,n+1):
    minimum = 4
    for j in range(1,int(i**(1/2))+1):
        if minimum > DP[i-j*j] : minimum = DP[i-j*j]
    DP.append(minimum+1)
print(DP[n])
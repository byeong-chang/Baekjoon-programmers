import sys
N = int(sys.stdin.readline())
point =[0,1,2]
for i in range(3,N+1):
    point.append(point[i-1]+point[i-2])
print(point[N]%10007)
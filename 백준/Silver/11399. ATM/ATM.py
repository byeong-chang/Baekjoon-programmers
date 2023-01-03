import sys
n = int(sys.stdin.readline())
timelist = list(map(int,sys.stdin.readline().split()))
timelist.sort()
sum=0
temp=0
for i in timelist:
    temp +=i
    sum +=temp
print(sum)
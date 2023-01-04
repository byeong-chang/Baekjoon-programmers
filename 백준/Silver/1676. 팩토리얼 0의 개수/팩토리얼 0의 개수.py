import sys
N = int(sys.stdin.readline())
sum =1
for i in range(N):
    sum*=(i+1)
flag = True
cnt=0
sum=str(sum)
while flag:
    if sum[-1-cnt] =="0":
        
        cnt+=1
    else :flag =False
print(cnt)
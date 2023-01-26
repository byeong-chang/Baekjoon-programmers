import math
M = int(input())
N = int(input())

sum =0
min_sosu =0
for i in range(M,N+1):
    sosu = True
    for j in range(2,int(math.sqrt(i))+1):
        
        if i %j ==0:
            sosu = False
            break
    if i == 1 : sosu=False
    if sum ==0 and sosu ==True:
        min_sosu = i
    if sosu ==True:
        sum +=i
if min_sosu ==0:
    print(-1)
else: print("{0}\n{1}".format(sum,min_sosu))
import sys
x = int(sys.stdin.readline())

dp_x = [0,0]
def factor_third(num):
    if num %3==0:
        return dp_x[num//3] + 1
    else : 
        return dp_x[num-1]+1

def factor_second(num):
    if num %2 == 0:
        return dp_x[num//2] + 1 
    else: 
        return dp_x[num-1]+1    

def minus_one(num):
    return dp_x[num-1]+1

for i in range(2,x+1):
    dp_x.append(min(factor_second(i),factor_third(i),minus_one(i)))

print(dp_x[x])
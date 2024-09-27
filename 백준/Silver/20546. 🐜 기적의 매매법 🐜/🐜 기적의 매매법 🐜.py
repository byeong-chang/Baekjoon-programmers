import sys

def input():
    return sys.stdin.readline().rstrip()

num = int(input())
lst = list(map(int, input().split()))

jun,junCount = num,0
for val in lst:
    if jun >= val:
        junCount += jun // val
        jun %= val
bnp = jun + lst[-1] * junCount

sung, sungCount, index = num,0,3
while index < 14:
    if lst[index] > lst[index-1] and lst[index-1] > lst[index-2] and lst[index-2] > lst[index-3]:
        sung += sungCount * lst[index]
        sungCount = 0
    if lst[index] < lst[index-1] and lst[index-1] < lst[index-2] and lst[index-2] < lst[index-3]:
        sungCount += sung // lst[index]
        sung %= lst[index]
    index +=1

timing = sung + lst[-1] * sungCount

if bnp > timing:
    print("BNP")
elif timing > bnp:
    print("TIMING")
else:
    print("SAMESAME")
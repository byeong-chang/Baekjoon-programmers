import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
Nlst = list(map(int, input().split()))
Nlst.sort()
M = int(input())
Mlst = list(map(int, input().split()))
mDict = {v : 0 for i,v in enumerate(Mlst)}
Mlst.sort()

index,length = 0,len(Nlst)
answer = []
for m in Mlst:
    while True:
        if index != length:
            if Nlst[index] < m:
                index +=1
                continue
            elif Nlst[index] == m:
                mDict[m] = 1
                break
            else: 
                mDict[m] = 0
                break
        else: 
            mDict[m] = 0
            break
print(*mDict.values())

import sys

def input():
    return sys.stdin.readline().rstrip()

n,m = map(int,input().split())
chickens = {}
answer = -1

for i in range(n):
    chickens[i] = list(map(int,input().split()))

sem = [0,0,0]
def comb(index,semIndex):
    global answer

    if semIndex == 3:
        temp = 0
        for j in range(n):
            temp += max([chickens[j][key] for key in sem])
        if temp > answer: 
            answer = temp
        return
    
    if index == m:
        return
    
    sem[semIndex] = index
    comb(index+1, semIndex+1)
    comb(index+1, semIndex)

comb(0,0)
print(answer)
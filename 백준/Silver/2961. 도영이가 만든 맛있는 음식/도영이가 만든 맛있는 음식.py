import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())

lst = [list(map(int,input().split())) for _ in range(N)]

sel = []
arr = [i for i in range(N)]
datas = []

def comb(idx,sidx,select):

    if sidx == select:
        datas.append(sel[::])
        return 
    
    if idx == N:
        return

    sel[sidx] = arr[idx]
    comb(idx+1,sidx+1,select)
    comb(idx+1,sidx,select)


answer = float('inf')
for i in range(1,N+1):
    sel = [0 for _ in range(i)]
    comb(0,0,i)

    for data in datas:
        sour,bitter = 1,0
        for idx in data:
            sour *= lst[idx][0]
            bitter += lst[idx][1]

        temp = abs(sour - bitter)
        if temp < answer:
            answer = temp
    datas = []
    

print(answer)
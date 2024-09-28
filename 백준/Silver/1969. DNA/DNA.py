import sys
def input():
    return sys.stdin.readline().rstrip()

N,M = map(int,input().split())
counting = [{"T" : 0,"G" : 0,"C" : 0,"A" : 0} for _ in range(M)]

for _ in range(N):
    dna = input()
    for i,val in enumerate(dna):
        counting[i][val] +=1

answer,distance = "",0

for dic in counting:
    maxVal,temp = 0,""
    for key,val in dic.items():
        if val >= maxVal:
            maxVal,temp = val, key
    answer += temp
    distance += N-maxVal

print(answer)
print(distance)

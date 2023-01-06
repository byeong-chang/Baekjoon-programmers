import sys
dogam = {}
dogam_reverse = {}
N,M = map(int,sys.stdin.readline().split())
for i in range(N):
    dogam[i+1] = sys.stdin.readline().strip()
    dogam_reverse[dogam[i+1]] = i+1

for j in range(M):
    ask = sys.stdin.readline().strip()
    if ask.isdigit():
        print(dogam[int(ask)])
    else:
        print(dogam_reverse[ask])
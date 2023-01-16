import sys
N = int(sys.stdin.readline())

times = [list(map(int,sys.stdin.readline().split())) for i in range(N)]
start = 0
end = 0
count = 0
times.sort(key = lambda x: (x[1],x[0]))
for i in times:
    if i[0] >=end:
        count+=1
        start = i[0]
        end = i[1]
print(count)
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N,M = map(int, sys.stdin.readline().rstrip().split(" "))
    big, small = max(N,M), min(N,M)
    
    result = 1
    for i in range(small):
        result *= (big-i)
        result /= (i+1) 

    print(int(result))
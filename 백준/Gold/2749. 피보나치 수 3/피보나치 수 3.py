import sys
N = int(sys.stdin.readline())
fib = [0,1]
for i in range(2,1500000):
    fib.append(fib[i-1]+fib[i-2])
    fib[i] %= 1000000
print(fib[N%1500000])
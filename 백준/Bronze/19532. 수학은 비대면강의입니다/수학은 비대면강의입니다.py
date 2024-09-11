import sys

a,b,c,d,e,f = map(int,sys.stdin.readline().rstrip().split())
y = (c * d - f * a) / (b * d - e * a)
x = (c * e - f * b) / (a * e - d * b)
print(int(x), int(y))
import sys
T =int(sys.stdin.readline())
add_123 = [0,1,2,4]
for i in range(4,12):
    add_123.append(add_123[i-1]+add_123[i-2]+add_123[i-3])

for i in range(T):
    print(add_123[int(sys.stdin.readline())])
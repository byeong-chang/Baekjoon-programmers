import sys

temp = [i for i in range(1,31)]
for i in range(28):
    num = int(sys.stdin.readline().rstrip())
    temp.remove(num)

temp.sort()
print(temp[0])
print(temp[1])


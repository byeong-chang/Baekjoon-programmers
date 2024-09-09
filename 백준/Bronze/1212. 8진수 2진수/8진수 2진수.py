import sys

def transform(number):
    number = int(number)
    temp = ""
    for _ in range(3):
        temp += str(number % 2)
        number = number // 2
    return temp[::-1]

num = sys.stdin.readline().rstrip()

temp = transform(num[0])
if temp[0] == "0": temp = temp[1:]
if temp[0] == "0": temp = temp[1:]
print(temp,end = "")

for i in range(1,len(num)):
    print(transform(num[i]),end = "")

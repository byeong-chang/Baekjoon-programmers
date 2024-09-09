import sys

num,form = sys.stdin.readline().rstrip().split(" ")
form = int(form)
alphabet = {chr(65+i) : 10+i for i in range(26)}
for i in range(10):
    alphabet[f"{i}"] = i

result,length = 0,len(num)
for i in range(length-1,-1,-1):
    result += alphabet[num[i]] * form ** (length - i-1)
    
if result > 1000000000:
    print(1000000000)
else:
    print(result)
import sys
current = sys.stdin.readline().rstrip().split(":")
late = sys.stdin.readline().rstrip().split(":")
result = []
prior = 0
for i in range(2,-1,-1):
    temp = int(late[i]) - int(current[i]) - prior
    prior = 0
    if temp < 0 :
        if len(result) == 2:
            temp +=24
        else:
            prior += 1
            temp +=60
    result.append(str(temp))

for i in range(len(result)):
    if len(result[i]) == 1:
        result[i] = "0" + result[i]

if result[0] == "00" and result[1] == "00" and result[2] == "00": print("24:00:00")
else: print(":".join(result[::-1]))

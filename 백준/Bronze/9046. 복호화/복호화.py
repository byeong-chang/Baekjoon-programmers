import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    text = sys.stdin.readline().rstrip().replace(" ", "")
    temp = {}
    for v in text:
        if v in temp:
            temp[v] +=1
        else: temp[v] = 1
    maxVal, doubleCheck, alphabet = 0, False, -1
    for key,val in temp.items():
        if val > maxVal:
            maxVal = val
            doubleCheck = False
            alphabet = key
        elif val == maxVal:
            doubleCheck = True

    if doubleCheck: print("?")
    else:   print(alphabet)
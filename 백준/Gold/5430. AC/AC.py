import sys
from collections import deque

for i in range(int(sys.stdin.readline())):
    p = sys.stdin.readline().strip()
    length = int(sys.stdin.readline())
    dq = deque(sys.stdin.readline().strip()[1:-1].split(','))
    
    if length == 0:
        dq = []

    flag = True
    rev = 0 
    for char in p:
        if char == 'R':
            rev +=1
        else:
            if rev%2 == 1:
                try :
                    dq.pop()
                except:
                    flag = False
                    break
            else:
                try :
                    dq.popleft()
                except:
                    flag = False
                    break
    dq = list(dq)
    if flag:
        if rev % 2 == 0:
            print("[" + ",".join(dq) + "]")
        else:
            dq.reverse()
            print("[" + ",".join(dq) + "]")
    else: 
        print('error')
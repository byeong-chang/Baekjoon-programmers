
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
    
pipes = input()
count,answer = 0,0
for i in range(len(pipes)):
    
    if pipes[i] == ")" and pipes[i-1] == "(":
        count -= 1
        answer += count
    elif pipes[i] == "(":
        count += 1
    else: 
        count -= 1
        answer += 1
print(answer)
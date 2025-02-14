
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
    
words = input()

if words[0] != "q"  or  words[-1] != "k" or len(words) % 5 :
    print(-1)
    exit()

checked = [False] * len(words)
answer = 0

completed = True
nextWord = "quack"
for i in range(len(words)-4):
    if words[i] == "q":
        start = False
        k = 0

        for j in range(i,len(words)):
            if words[j] == nextWord[k] and not checked[j]:
                if words[j] == "k":
                    if not start:
                        answer +=1
                        start = True
                    k = -1

                checked[j] = True
                k+=1

if answer == 0 or sum(checked) != len(words): print(-1)
else: print(answer)

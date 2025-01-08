import sys
def input():
    return sys.stdin.readline().rstrip()

N,S = map(int,input().split())
data = list(map(int,input().split()))
count = 0

def bruteForce(idx, total):
    global count
    
    if idx >= N:
        return

    bruteForce(idx+1, total)
        
    total += data[idx]

    if total == S:
        count+=1
    
    bruteForce(idx+1,total)


bruteForce(0,0)
print(count)
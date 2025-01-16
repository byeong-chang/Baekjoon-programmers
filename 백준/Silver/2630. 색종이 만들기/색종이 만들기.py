import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
nums = [list(map(int,input().split())) for _ in range(N)]
answer = {0:0,1:0}

def check(count,x,y):
    
    start = nums[x][y]
    flag = True
    for i in range(count):
        if not flag:
            break

        for j in range(count):
            if nums[x+i][y+j] != start:
                flag = False
                break
    if flag:
        # 모두 같은색이라면 return
        answer[start] +=1
        return
    
    # 모두 같은색이 아니라면 잘라서 다시 실행
    
    count //=2
    check(count,x,y)
    check(count,x+count,y)
    check(count,x,y+count)
    check(count,x+count,y+count)

check(N,0,0)

print(answer[0])
print(answer[1])
    


import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
# map(int,input().split())

n = int(input())
c = int(input())
answer = {}
lst = list(map(int,input().split()))
    
for i in range(c):
    # 일단 추가하고
    if lst[i] in answer:
        answer[lst[i]][0] += 1
        # answer[lst[i]][1] = i
    else:   
        #개수 넘기면
        if len(answer) > n-1:
            # 가장 추천이 적으면 삭제
            small = min(answer.values() , key = lambda x: x[0])[0]
            index = [key for key,val in answer.items() if val[0] == small]
            
            # 추천 적은 학생이 겹친다면 가장 오래되면 삭제
            if len(index) == 1:
                answer.pop(index[0])
            else:
                oldIndex = min(index , key = lambda x: answer[x][1])
                answer.pop(oldIndex)
        #지우고 추가
        answer[lst[i]] = [1,i]

    # print(answer)
print(*sorted(answer.keys()))
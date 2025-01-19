
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
    
N = int(input())

for _ in range(N):
    # 값 받고
    lst = []
    for _ in range(3):
        temp = input().split()
        for v in temp:
            if v == "H": lst.append('1')
            else: lst.append('0')
    
    # 시작값 선언.
    cases = [[0,1,2], [3,4,5], [6,7,8], [0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    answer = float('inf')
    visited = [0] * 512
    visited[int(''.join(lst),2)] = 1
    queue = deque([lst])

    # 시작부터 완성형인경우
    if int(''.join(lst),2) == 511 or int(''.join(lst),2) == 0: 
        print(0)
        continue

    # BFS 수행
    while queue:
        arr = queue.popleft()
        count = visited[int(''.join(arr),2)]

        # 현재값 기준 모든 케이스에 대해 조사
        for case in cases:
            temp = arr[::]
            for i in case:
                if temp[i] == '1': temp[i] = '0' 
                else: temp[i] = '1'

            validation = int("".join(temp),2)
            if visited[validation] == 0:
                visited[validation] = count+1
                queue.append(temp)

                if (validation == 511 or validation == 0) and count < answer:
                    answer = count

    if answer != float("inf"): print(answer)
    else: print(-1)
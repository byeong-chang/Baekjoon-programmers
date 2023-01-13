# [Silver II] 연결 요소의 개수 - 11724 

[문제 링크](https://www.acmicpc.net/problem/11724) 

### 풀기 실패

### 문제 고찰
1. 그래프긴 한데.. 뭐로 풀어야 할지 잘 모르겠다.
2. 알고리즘 분류 확인 후 DFS,BFS임을 확인함.
3. 함수 짜는 것을 공부중이라 BFS로 풀기로함.
4. for 문으로 리스트 읽어들여서 다 연결하고,
5. 연결된 놈들을 check_list를 만들어 체크한다.

### 시간초과 난 코드
```python
import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())
edge_lst = [list(map(int,sys.stdin.readline().split())) for i in range(M)]
check_lst = [False for i in range(N)]
count = 0

def connected(N):
    Q = deque()
    Q.append(N)
    remove_lst =[]
    global count
    while Q:
        value = Q.popleft()+1
        for i in edge_lst:
            if value in i:
                if check_lst[i[0]-1] == False:
                    check_lst[i[0]-1] = True
                    Q.append(i[0]-1)
                if check_lst[i[1]-1] == False:
                    check_lst[i[1]-1] = True
                    Q.append(i[1]-1)
                if i not in remove_lst:
                    remove_lst.append(i)
    count+=1
    for i in remove_lst:
        edge_lst.remove(i)

for i in range(N):
    if check_lst[i] == True: 
        continue
    else:
        connected(i)
print(count)
```


### 성능 요약

메모리: 194124 KB, 시간: 584 ms

### 분류

그래프 이론(graphs), 그래프 탐색(graph_traversal), 너비 우선 탐색(bfs), 깊이 우선 탐색(dfs)

### 문제 설명

<p>방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.</p>

### 출력 

 <p>첫째 줄에 연결 요소의 개수를 출력한다.</p>


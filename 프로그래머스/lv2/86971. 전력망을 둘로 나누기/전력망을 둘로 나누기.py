def dfs(start,graph):
    stack = [start]
    visited = []
    while stack:
        now = stack.pop()
        if now not in visited:
            visited.append(now)
            
        for i in range(len(graph)):
            if graph[now][i] and i not in visited:
                stack.append(i)
    print(visited)
    return len(visited)

def solution(n, wires):
    
    # 인접행렬 만들어버리고, 
    # wires로 for문을 돌린다
    # 하나의 wire마다 인접행렬의 연결을 끊어주고, 다시 되돌리는 코드를 만든다.
    # 인접행렬의 연결이 끊긴 상태에서 끊긴 지점에 대한 dfs를 돌려 node의 개수를 찾는다.
    # ex) wire가 [1,3]이면 둘의 연결을 끊고, 1을 시작점으로 dfs를 돌려 node개수 찾기 + 3을 시작점으로 dfs를 돌려 node개수 찾기 + 다시 원래 인접행렬로 되돌리기
    
    answer = 100
    graph = [[0]*(n+1) for _ in range(n+1)]
    for wire in wires:
        graph[wire[0]][wire[1]] = 1
        graph[wire[1]][wire[0]] = 1
        
    for wire in wires:
        graph[wire[0]][wire[1]] = 0
        graph[wire[1]][wire[0]] = 0
        
        a = dfs(wire[0],graph)
        b = dfs(wire[1],graph)
        
        if answer > abs(a-b):
            answer = abs(a-b)
            
        graph[wire[0]][wire[1]] = 1
        graph[wire[1]][wire[0]] = 1
        
    return answer
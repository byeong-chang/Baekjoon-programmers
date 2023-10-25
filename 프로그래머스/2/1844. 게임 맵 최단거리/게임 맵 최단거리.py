def solution(maps):
    '''
    재귀 bfs dfs 로 풀어보자
    현 위치 기준 4방향 재귀함수 실행
    n,m에 도달시 길이 반환 최소값 검토
    최소값 return or n,m에 도달 못함 -> -1 반환
    '''
    xval = [-1,1,0,0]
    yval = [0,0,-1,1]
    m,n = len(maps),len(maps[0])
    stack = [[0,0]]
    count = 0
    while stack:
        count+=1
        x,y = stack.pop(0)
        for i in range(4):
            dx = x + xval[i]
            dy = y + yval[i]
            if dx <0 or dx >=n or dy <0 or dy >=m:
                continue
            else:
                if maps[dy][dx] == 1:
                    stack.append([dx,dy])
                    maps[dy][dx] = maps[y][x] +1
                elif maps[dy][dx] == 0:
                    continue
                else:
                    maps[dy][dx] = min(maps[dy][dx],maps[y][x]+1)
    print(count)
    if maps[m-1][n-1] == 1:
        return -1
    else: return maps[m-1][n-1]
def solution(dirs):
    '''
    11 X 11 배열을 만들고, LRUD 한칸당(점기준) 4개만 들어올 수 있도록 제한을 건다.
    방향 입력이 들어올 경우 처음 장소 -> 원하는 지점, 원하는 지점 -> 처음 장소 두 방향 모두 선을 그어준다.
    들어온 방향에 개수에 대해 세려주고 전체 길이 합계//2가 반환값임.
    '''
    # 그래프 만들기
    graph = []
    for _ in range(11):
        graph.append([[] for _ in range(11)])
    #시작점 지정 및 directory 생성
    start = [5,5]
    direction = {'U':[0,1],'D':[0,-1],'L':[-1,0],'R':[1,0]}
    reverse = {'U' : 'D', 'D' : 'U', "L":"R" , "R" : 'L'}
    # 그래프 채우기
    for d in dirs:
        dx = start[0] + direction[d][0]
        dy = start[1] + direction[d][1]
        if dx < 0 or dx > 10 or dy < 0 or dy > 10:
            continue
        if d not in graph[dy][dx]:
            graph[dy][dx].append(d)
            graph[start[1]][start[0]].append(reverse[d])
        start = [dx,dy]
    # 길이 구하기
    answer = 0
    for line in graph:
        for val in line:
            answer += len(val)
    return answer//2
        

answer = 0
visited = []

def dfs(dungeons, energy, cnt):
    global answer
    if cnt > answer:
        answer = cnt
    for i in range(len(dungeons)):
        if not visited[i] and energy >= dungeons[i][0]:
            visited[i] = 1
            dfs(dungeons,energy - dungeons[i][1], cnt+1)
            visited[i] = 0
def solution(k, dungeons):
    global answer,visited
    visited = [0] * len(dungeons)
    dfs(dungeons,k,0)
    return answer
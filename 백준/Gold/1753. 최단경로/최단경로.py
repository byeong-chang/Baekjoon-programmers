import heapq
import sys
def dijkstra(start):
    q= []
    heapq.heappush(q,(0,start))
    answer[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        # 현재 저장된 값보다 가중치가 크면 바로 패스
        if answer[now] < dist:
            continue

        #현재 노드와 연결된 인접 노드 확인
        for i in edges[now]:
            cost = dist+ i[1]
            if cost < answer[i[0]] :
                answer[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

INF = int(1e9)
V,E = list(map(int,sys.stdin.readline().split()))
start = int(sys.stdin.readline())
answer = [INF for _ in range(V+1)]
answer[start] = 0
# edge값 저장
edges = { _ : [] for _ in range(1,V+1)}
for i in range(E):
    temp = list(map(int,sys.stdin.readline().split()))
    edges[temp[0]].append([temp[1],temp[2]])

dijkstra(start)

for i in range(1,V+1):
    if answer[i] == INF:
        print('INF')
    else:
        print(answer[i])
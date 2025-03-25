import sys
import math

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [[int(a) for a in input()] for _ in range(n)]
answer = -1

# 등차수열로 이동할 수 있는 모든 방향 생성
directions = []
for dx in range(-max(n, m), max(n, m) + 1):
    for dy in range(-max(n, m), max(n, m) + 1):
        if dx == 0 and dy == 0:
            continue  # 정지하는 경우 제외
        directions.append((dx, dy))

# 모든 위치에서 시작하여 가능한 모든 숫자를 만들어 봄
for x in range(m):
    for y in range(n):
        for dx, dy in directions:
            tx, ty = x, y
            temp = 0

            while 0 <= tx < m and 0 <= ty < n:
                temp = temp * 10 + graph[ty][tx]

                # 완전 제곱수인지 확인
                if math.isqrt(temp) ** 2 == temp:
                    answer = max(answer, temp)

                tx += dx
                ty += dy

print(answer)
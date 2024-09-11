import sys

N = int(sys.stdin.readline().rstrip())
temp = N
count = 0
while True:
    count += 1

    # 원래값 오른쪽
    before = temp % 10
    # 더한값 오른쪽
    after = (temp // 10 + temp % 10) % 10

    temp = 10 * before + after

    if temp == N:
        break

print(count)
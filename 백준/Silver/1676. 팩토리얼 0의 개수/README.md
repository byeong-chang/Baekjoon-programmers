# [Silver V] 팩토리얼 0의 개수 - 1676 

[문제 링크](https://www.acmicpc.net/problem/1676) 

### 2회 시도
딱 보고 greedy임을 알아챘다. (뿌듯..)
다만 2회 시도 한 것으로는 큰 coin부터 하나씩 빼주고 count를 1씩 늘려주는 하나씩 카운팅 하는 방식으로 진행했으나 시간 초과가 발생했고, 몫과 나머지를 구하는 // % 연산을 통해 빠르게 각 coin별 사용 횟수를 얻어 해결함.

```python
#틀린코드
import sys
N,K = map(int,sys.stdin.readline().split())
coins =[]
count =0
for i in range(N):
    coins.append(int(sys.stdin.readline()))
coins.reverse()
for _ in coins:
    while True:
        if K >= _:
            K -=_
            count+=1
        else: break
print(count)
```

### 성능 요약

메모리: 30616 KB, 시간: 36 ms

### 분류

임의 정밀도 / 큰 수 연산(arbitrary_precision), 수학(math)

### 문제 설명

<p>N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)</p>

### 출력 

 <p>첫째 줄에 구한 0의 개수를 출력한다.</p>


# [Gold V] 리모컨 - 1107 

[문제 링크](https://www.acmicpc.net/problem/1107) 

### 7회 시도
자리수 별로 시도해보려 했으나 모든 경우를 조사하지 못했다.
알고리즘 방식이 brute force임을 확인했으나 이정도로 모든 경우를 조사할줄은 몰랐다..
##### 틀린 코드
```python
mport sys
N = sys.stdin.readline()
N = N.rstrip()
M = int(sys.stdin.readline())
if M == 0:
    print(len(N))
    exit()
error =list(map(int,sys.stdin.readline().split()))
control = [0,1,2,3,4,5,6,7,8,9]
for i in error:
    del control[control.index(i)]
count=0
decimal = len(N)-1
for i in N:
    diff =1
    if int(i) in control:
        count +=1
        decimal -=1
    else: 
        while True:
            if int(i)+diff in control or  int(i) -diff in control:
                if decimal ==0:
                    count +=(diff+1)
                    break
                else: 
                    count +=(diff*10**decimal+1)
                    decimal -=1
                    break
            elif diff >=9:
                count += (int(i)*10**decimal)
                decimal -=1
                break
            else : diff +=1
print(min(count,abs(int(N)-100)))
```

### 성능 요약

메모리: 30616 KB, 시간: 2172 ms

### 분류

브루트포스 알고리즘(bruteforcing)

### 문제 설명

<p>수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.</p>

<p>리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다. 채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.</p>

<p>수빈이가 지금 이동하려고 하는 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오. </p>

<p>수빈이가 지금 보고 있는 채널은 100번이다.</p>

### 입력 

 <p>첫째 줄에 수빈이가 이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)이 주어진다.  둘째 줄에는 고장난 버튼의 개수 M (0 ≤ M ≤ 10)이 주어진다. 고장난 버튼이 있는 경우에는 셋째 줄에는 고장난 버튼이 주어지며, 같은 버튼이 여러 번 주어지는 경우는 없다.</p>

### 출력 

 <p>첫째 줄에 채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는지를 출력한다.</p>


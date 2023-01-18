# [Silver I] IOIOI - 5525 

[문제 링크](https://www.acmicpc.net/problem/5525) 

### 2회시도 
서브테스크 문제였고, brute force로 접근하여 첫 시도에 50점을 맞아서 다시 풀게 되었다. 풀이법은 반복문 하나만 사용하여 
bruteforce가 아닌 중간중간 뛰어 넘어 해결하면 complexity가 낮아져 맞는 풀이가 되었다.

### 50점 코드
import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline()
Pn = 'I'+'OI' *N
str_len = len(Pn)
S_len = len(S)
count=0
for i in range(S_len):
    if S[i] =='I'and S_len - i >= str_len:
        if S[i:i+str_len] == Pn:
            count+=1
print(count)

### 성능 요약

메모리: 30616 KB, 시간: 36 ms

### 분류

문자열(string)

### 문제 설명

<p>N+1개의 <code>I</code>와 N개의 <code>O</code>로 이루어져 있으면, <code>I</code>와 <code>O</code>이 교대로 나오는 문자열을 P<sub>N</sub>이라고 한다.</p>

<ul>
	<li>P<sub>1</sub> <code>IOI</code></li>
	<li>P<sub>2</sub> <code>IOIOI</code></li>
	<li>P<sub>3</sub> <code>IOIOIOI</code></li>
	<li>P<sub>N</sub> <code>IOIOI...OI</code> (<code>O</code>가 N개)</li>
</ul>

<p><code>I</code>와 <code>O</code>로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 P<sub>N</sub>이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 N이 주어진다. 둘째 줄에는 S의 길이 M이 주어지며, 셋째 줄에 S가 주어진다.</p>

### 출력 

 <p>S에 P<sub>N</sub>이 몇 군데 포함되어 있는지 출력한다.</p>


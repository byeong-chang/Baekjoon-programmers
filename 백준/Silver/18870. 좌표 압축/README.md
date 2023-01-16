# [Silver II] 좌표 압축 - 18870 

[문제 링크](https://www.acmicpc.net/problem/18870) 

### 2회시도 = 시간초과
방법1 일단 정렬해서 len()연산과 사용하여 정리한다.
= python sort() = nlogn이고, 내가 만든 연산도 n보단 클것임.
= n^2*logn
방법2 brute force = n +n-1+n-2.. n(n+1)/2 = n^2
방법 1을 채택함
성공한 코드와 비교했을 때 정렬된 값을 dict에 저장하는 방식에서 한번 더 연산을 하는 방법이었기에 시간초과가 발생하여 틀리게 되었다.  
조금 더 로직이 간단했다면 좋았을듯

### 틀린 코드
```python
import sys

n = int(sys.stdin.readline())
input_save = list(map(int,sys.stdin.readline().split()))
sorted_values = sorted(list(set(input_save)),reverse=True)
value_index = {}
for i in sorted_values:
        value_index[i] = len(sorted_values)-sorted_values.index(i)-1
for i in input_save:
    print(value_index[i],end=" ")
```
### 성능 요약

메모리: 150180 KB, 시간: 1900 ms

### 분류

값 / 좌표 압축(coordinate_compression), 정렬(sorting)

### 문제 설명

<p>수직선 위에 N개의 좌표 X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>N</sub>이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.</p>

<p>X<sub>i</sub>를 좌표 압축한 결과 X'<sub>i</sub>의 값은 X<sub>i</sub> > X<sub>j</sub>를 만족하는 서로 다른 좌표의 개수와 같아야 한다.</p>

<p>X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>N</sub>에 좌표 압축을 적용한 결과 X'<sub>1</sub>, X'<sub>2</sub>, ..., X'<sub>N</sub>를 출력해보자.</p>

### 입력 

 <p>첫째 줄에 N이 주어진다.</p>

<p>둘째 줄에는 공백 한 칸으로 구분된 X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>N</sub>이 주어진다.</p>

### 출력 

 <p>첫째 줄에 X'<sub>1</sub>, X'<sub>2</sub>, ..., X'<sub>N</sub>을 공백 한 칸으로 구분해서 출력한다.</p>


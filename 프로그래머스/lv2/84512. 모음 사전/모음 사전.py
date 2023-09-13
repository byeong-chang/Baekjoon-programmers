'''
1.입력받은 문자의 길이별 + 문자별 조건식?
2.BruteForce니까 로직만 짜서 1씩 증가? <- 이래도 되는게 가장 큰 수 해봐야 5^5임 시간초과는 안날걸
2번으로 진행해보도록 하고, 로직은 어떻게 하느냐가 문제일듯
'''
from itertools import product
def solution(word):
    answer = []
    for i in range(1,6):
        for v in product(["A","E","I","O","U"],repeat = i):
            answer.append("".join(v))
    answer.sort()
    return answer.index(word)+1
from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    dic = defaultdict(int) # 처음 입력될 때 0으로 선언되는 놈인가봄
# 원래는 tangerine의 원소가 10,000,000 까지래서 10,000,000개의 메모리를 사용하려 했는데, 메모리 초과날듯해서 라이브러리 찾아봄
    for i in tangerine:
        dic[i] +=1
    dic = list(dic.items())
    dic.sort(key = lambda x : x[1], reverse = True)
    while k > 0:
        k-= dic[answer][1]
        answer+=1
        
    
    return answer
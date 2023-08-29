def solution(clothes):
    # 보자마자 수학문제라는 생각이 들었다.
    # 분류별로 dict 자료형에 담아서 value의 개수를 세려 뭔가 공식을 사용하면 답이 나올 것 같은 기분이 들었다.
    dict_cloth = dict()
    answer = 1
    for cloth in clothes:
        if cloth[1] in dict_cloth:
            dict_cloth[cloth[1]] +=1
        else: 
            dict_cloth[cloth[1]] = 1
    for num in dict_cloth.values():
        answer *= (num+1) 
    return answer-1
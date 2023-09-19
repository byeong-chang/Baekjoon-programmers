# 우선 문자열 처리가 수행되어야한다. 대소문자 구분을 위해 upper나 lower를 적용시켜준다.
# 특수 문자, 공백, 숫자,등의 경우는 제거해서 2단어에 대해 리스트화 시킨다.(어떤 것들이 있는지 모르니까 a-z 사이만 허용하도록 설정)
# 합집합, 교집합을 구하는 공식을 따로 적용하여 계산까지 하면 될듯
import re

def solution(str1, str2):
    alphabet = re.compile('[a-z]')
    arr1,arr2 = [],[]
    intersection, union = 0,[]
    str1 = str1.lower()
    str2 = str2.lower()
    #str1 걸러주고 리스트에 저장
    for i in range(len(str1) -1 ):
        if alphabet.match(str1[i]) and alphabet.match(str1[i+1]):
            arr1.append(str1[i] + str1[i+1])
    for i in range(len(str2) -1 ):
        if alphabet.match(str2[i]) and alphabet.match(str2[i+1]):
            arr2.append(str2[i] + str2[i+1])
    
    temp = arr2.copy()
    # 교집합 구하기
    for one in arr1:
        if one in temp:
            temp.remove(one)
            intersection +=1
    # 합집합 구하기 - {1,1,2,3} U {1,2,2,3} 의 경우 11223 이 되어야 해서 어렵더라(중복처리)
    union = arr2.copy()
    for one in arr1:
        if one not in arr2: 
            union.append(one)
        else: 
            arr2.remove(one) 
    union = len(union)
    # 교집합, 합집합을 구했는데 한쪽이 0 이면 나누지 못하기 때문에 1 * 65536 반환
    if union == 0 :
        return 65536
    elif intersection == 0:
        return 0
    else: return (intersection / union * 65536) // 1
    
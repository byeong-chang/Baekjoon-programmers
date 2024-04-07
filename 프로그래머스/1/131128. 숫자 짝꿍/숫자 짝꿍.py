def solution(X, Y):
    answer = []
    # 겹치는 숫자들 answer에 모음
    # 큰 수부터 처리함으로써 나중에 sort 안해도 되게끔 유도
    for i in range(9,-1,-1):
        answer.append(str(i) * min(X.count(str(i)), Y.count(str(i))))
    
    # 문자열들을 다 합치고 연산
    string = ''.join(answer)
    if not string: return '-1'
    # 다 0이면 '000'으로 출력되지 않고, 0으로 처리하도록 조건 분기
    elif len(string) == string.count('0'):
        return '0'
    else: 
        return string
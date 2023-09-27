def solution(X, Y):
    answer = []
    for i in range(9,-1,-1):
        answer.append(str(i) * min(X.count(str(i)), Y.count(str(i))))
    string = ''.join(answer)
    if not string: return '-1'
    elif len(string) == string.count('0'):
        return '0'
     
    else: return string
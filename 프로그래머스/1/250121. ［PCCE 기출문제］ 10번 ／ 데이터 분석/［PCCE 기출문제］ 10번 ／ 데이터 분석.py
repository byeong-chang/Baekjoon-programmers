'''
ext, val_ext 기준으로 데이터를 고르고 그 데이터를 정렬한다?
db 쿼리같네
순서만 바꿔서 sort_by기준으로 정렬 후 val_ext 기준으로 조건 통과한 애만 배열에 담아서 리턴
'''

def solution(data, ext, val_ext, sort_by):
    type_dic = {'code': 0 , 'date' : 1 , 'maximum' : 2, 'remain' :3}
    data = sorted(data, key = lambda x : x[type_dic[sort_by]])
    answer = []
    for val in data:
        if val[type_dic[ext]] <val_ext:
            answer.append(val)
    return answer
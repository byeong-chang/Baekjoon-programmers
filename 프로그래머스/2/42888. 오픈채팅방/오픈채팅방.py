def solution(record):
    # 열이 2개인 리스트 만들어서 userId랑 입출력 문자열 넣어주고, change가 들어오면 수정해준다
    # n이 10만이니까 시간초과는 안날거 같은데 더 효율적인 방법은 없을까
    # dict써서
    records = [i.split() for i in record]
    answer = []
    user = {}
    for record in records:
        if record[0] == 'Enter':
            user[record[1]] = record[2]
            answer.append(record[1] + '님이 들어왔습니다.')
        elif record[0] == 'Leave':
            answer.append(record[1]+ '님이 나갔습니다.' )
        elif record[0] == "Change":
            user[record[1]] = record[2]
    submit = []
    for val in answer:
        name,way = val.split()
        name = user[name[:-2]]
        submit.append(name + '님이 '+ way)
    return submit
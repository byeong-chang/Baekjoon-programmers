def solution(new_id):
    #1단계
    new_id = new_id.lower()
    #2단계
    for i in ['~','!','@','#','$','%','^','&','*','(',')','=','+','[','{',']','}',':','?',',','<','>','/']:
        new_id = new_id.replace(i,'')
    #3단계
    temp = len(new_id)
    while True:
        new_id = new_id.replace('..','.')
        if len(new_id) == temp:
            break
        else: temp = len(new_id)
    #4단계
    if new_id and new_id[0] == '.': new_id = new_id[1:]
    if new_id and new_id[-1] == '.': new_id = new_id[:-1]
    #5단계
    if not new_id : new_id +='a'
    #6단계
    if len(new_id) >=16: 
        new_id = new_id[:15]
        if new_id[-1] == '.': new_id = new_id[:-1]
    #7단계
    while len(new_id) <3:
        new_id += new_id[-1]
    return new_id
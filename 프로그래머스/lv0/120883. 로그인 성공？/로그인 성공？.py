def solution(id_pw, db):
    for data in db:
        if id_pw == data:
            return "login"
        elif id_pw[0] == data[0]:
            return "wrong pw"
    return "fail"
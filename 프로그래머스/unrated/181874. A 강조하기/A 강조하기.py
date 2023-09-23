def solution(myString):
    myString = myString.lower()
    answer = ''
    for val in myString:
        if val == 'a':
            answer+="A"
        else: answer+= val
    return answer
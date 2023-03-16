def solution(s):
    answer = ''
    words = []
    temp = ""
    for i in s:
        temp +=i
        if i == " ":
            words.append(temp)
            temp = ""
    if temp != "":
        words.append(temp)
    
    for text in words:
        if text[0] == "":
            answer += text
        else:
            answer += text[0].upper()
            answer += text[1:].lower()
    return answer
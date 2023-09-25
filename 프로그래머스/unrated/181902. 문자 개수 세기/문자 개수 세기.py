def solution(my_string):
    answer = [0 for i in range(52)]
    for word in my_string:
        if word.isupper():answer[ord(word)-65]+=1
        else: answer[ord(word) - 71]+=1
    return answer
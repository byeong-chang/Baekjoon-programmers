def solution(my_string):
    answer = 0
    my_string = my_string.split()
    print(my_string)
    answer += int(my_string[0])
    for i in range(len(my_string)//2):
        if my_string[i*2 + 1] == "+":
            answer += int(my_string[i*2 +2])
        else: answer -= int(my_string[i*2 +2])
    return answer
def solution(my_string, s, e):
    answer = my_string[:s] +my_string[s:e+1][::-1]+ my_string[e+1:]
    print(my_string[e:s-1:-1])
    return answer
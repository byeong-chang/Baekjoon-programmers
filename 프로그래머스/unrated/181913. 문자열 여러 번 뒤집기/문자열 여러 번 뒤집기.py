def solution(my_string, queries):
    for query in queries:
        s,e = query[0],query[1]
        my_string = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    return my_string
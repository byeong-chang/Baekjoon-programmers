def solution(n_str):
    answer = ''
    for n in range(len(n_str)):
        if n_str[n] != '0':
            return n_str[n:]
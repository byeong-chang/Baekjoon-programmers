def solution(my_string, is_prefix):
    length = len(is_prefix)
    if my_string[:length] == is_prefix:
        return 1
    else: return 0
    
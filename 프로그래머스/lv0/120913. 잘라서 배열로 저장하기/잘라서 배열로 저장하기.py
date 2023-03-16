def solution(my_str, n):
    answer = []
    for i in range(len(my_str)//n):
        answer.append(my_str[i*n:(i+1)*n])
    if len(my_str) % n != 0:
        last = len(my_str)//n 
        answer.append(my_str[last*n:])
    return answer
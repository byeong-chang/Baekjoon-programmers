def solution(num_list):
    odd = len([i for i in num_list if i% 2 == 1])
    even =len([i for i in num_list if i%2 == 0])
    answer = [even,odd]
    return answer
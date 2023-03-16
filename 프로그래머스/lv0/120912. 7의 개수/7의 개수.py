def solution(array):
    answer = 0
    for val in array:
        for _ in str(val):
            if _ == "7":
                answer +=1
    return answer
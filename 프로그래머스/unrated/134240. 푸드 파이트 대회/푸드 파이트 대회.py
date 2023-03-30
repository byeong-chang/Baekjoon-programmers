def solution(food):
    temp = ''
    for index, f in enumerate(food):
        if f %2 == 1: f-=1
        for i in range(f//2):
            temp += str(index)
            
    answer = temp + "0"+temp[::-1]
    return answer
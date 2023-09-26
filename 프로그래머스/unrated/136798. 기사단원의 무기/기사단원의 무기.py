def measure(num):
    temp = 0
    for i in range(1,int(num**(0.5))+1):
        if num%i == 0:
            temp +=1
            if i**2 != num:
                temp+=1
    return temp
def solution(number, limit, power):
    answer = 0
    measures = [measure(i) for i in range(1,number+1)]
    for mes in measures:
        if mes <= limit:
            answer += mes
        else: answer += power
    return answer
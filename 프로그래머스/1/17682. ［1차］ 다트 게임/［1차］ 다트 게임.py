'''
초기 목표는 기회별로 자르는 것이었다.
다만 문자열에 구분이 없고, 옵션의 여부도 확실하지 않으며, 10이라는 변수 때문에 포기하였다
우선 숫자 값을 먼저 뽑고, 그 숫자가 있는 인덱스도 저장하여 조건문으로 처리하였다.
'''
def solution(dartResult):
    #숫자 뽑는 코드
    num_range = [str(num) for num in range(0,11)]
    index = 0
    chances = []
    pointer = -1
    while len(chances)<3:
        pointer +=1
        current = dartResult[pointer]
        if current in num_range:
            if dartResult[pointer:pointer +2] == '10':
                chances.append([10,pointer+2])
                pointer +=1
            else: 
                chances.append([int(dartResult[pointer]),pointer+1])
            index +=1
    # 나머지 문자 받아서 연산 코드
    answer = []
    for chance,i in chances:
        if dartResult[i] == 'D':
            answer.append(chance**2)
        elif dartResult[i] == 'T':
            answer.append(chance**3)
        else: 
            answer.append(chance)
            
        i +=1
        if i != len(dartResult):
            if dartResult[i] == '#':
                answer[-1]*=(-1)
            elif dartResult[i] == '*':
                if len(answer) ==1:
                    answer[-1]*=2
                else: 
                    answer[-1] *=2
                    answer[-2] *=2
    return sum(answer)
        

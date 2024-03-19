'''
아이디어 : 소수판별이 일단 필요하며, set에 소수들 추가하며, 중복처리는 신경쓰지 않는다.
에라토네스의 체를 구현해볼까 했지만 number 이하의 소수들을 결국 구해야 하기에 소수판별 코드 2개 사용하고 싶지 않아서 다른 방법을 사용했다.
'''
def decimal(num):
    decimal_set = set()
    for i in range(1, int(num **(1/2))+1):
        if num % i == 0 :
            decimal_set.add(i)
            decimal_set.add(num//i)
    return len(decimal_set)
    
def solution(number, limit, power):            
    answer = 0
    
    for num in range(1,number+1):
        length = decimal(num)
        if length > limit:
            answer += power
        else: answer += length
        
    return answer
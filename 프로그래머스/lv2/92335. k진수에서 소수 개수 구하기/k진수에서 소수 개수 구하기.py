def conv2k(n,k):
    num = ''
    while n>0:
        num = str(n % k) + num
        n //=k
    return num
def is_prime(n):
    if n <2:
        return False
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
# 10진수 숫자 n을 k진수로 변환하고, 문자열로 만들어서 저장
# 문자열을 읽으며 조건에 맞는 상황에 도달하면 0 을 만나는 경우 끊으면 뭔가 될 것 같은데
def solution(n, k):
    answer = 0
    nums = conv2k(n,k) 
    for num in nums.split("0"):
        print(num)
        if len(num) >0:
            if is_prime(int(num)):
                answer+=1
    
    return answer
global cases,sel,check

def perm(depth,nums, length):  # 각자 뎁스에서는? 
    global check,sel,cases
    if depth == length:  # 최고 뎁스에 도달했으면? # if depth == len(sel)
        cases.append(int(''.join(sel)))
        return
    
    for i in range(length):  # 3번의 화살표 떨어트릴 기회
        if not check[i]:  # 각 기회 안에서 check를 보고 멈출 수 있는지 보고?
            check[i] = 1  # 멈출 수 있다면 if 통과했으니까 자리 차지했다고 표시하고
            sel[depth] = nums[i]  # 화살표가 떨어진 위치의 재료리스트
            perm(depth+1,nums,length)
            check[i] = 0  # 돌아나오면서 다시 다음을 위해 초기화!! (중요)


def isPrime(num):
    if num <2:
        return False
    for i in range(2,num//2+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    # 1. 가진 숫자로 모든 경우를 조합하는 방법
    # 2. 소수판별 알고리즘
    # 2가지 로직이 필요한데, 2번이야 간단하게 2 ~ num/2인 경우랑 비교해서 나눠떨어지면 넘겨주고,
    # BruteForce로 조합가능한 리스트를 만들고 set 씌워서 중복처리 하는것도 괜찮을듯.
    answer = 0
    global sel,check,cases
    cases = []
    #모든 경우 조합
    for i in range(len(numbers)):
        sel = [ '' for _ in range(len(numbers))]
        check = [ 0 for _ in range(len(numbers))]
        perm(i,numbers,len(numbers))
    #중복 제거
    cases = list(set(cases))
    #소수 판별
    for case in cases:
        if isPrime(case):
            answer+=1
    return answer
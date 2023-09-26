def gcd(n1,n2):
    while n2 >0:
        n1,n2 = n2 , n1%n2
    return n1

def solution(denum1, num1, denum2, num2):
    # 1. 두 분수의 합 계산
    boonmo = num1 * num2
    boonja = denum1 * num2 + denum2 * num1
    
    # 2. 최대공약수 계산
    gcd_value = gcd(boonmo, boonja)

    # 3. gcd 로 나눈 값을 answer에 담기
    answer = [boonja / gcd_value, boonmo / gcd_value]
    return answer


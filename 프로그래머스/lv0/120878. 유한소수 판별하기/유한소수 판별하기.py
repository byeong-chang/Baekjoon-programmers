def gcd(a, b) :
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def solution(a, b): # 최대 공약수
    answer = []
    GCD = gcd(a,b)
    b //= GCD
    while b >1: 
        print(b)
        for i in range(2,b+1):
            if b%i == 0:
                if i != 2 and i != 5:
                    return 2
                answer.append(i)
                b//=i
                break
    return 1

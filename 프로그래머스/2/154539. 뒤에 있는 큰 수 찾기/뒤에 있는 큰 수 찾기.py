'''
2중 for문 돌려서 풀면 n^2 시간복잡도 걸리고 n의 길이는 1,000,000이니까 시간초과 문제인듯
구현이 어렵지 않아서 1분정도 써서 2중 for문 만들어봤는데 4개 케이스가 시간초과였음.
도저히 새로운 방법이 떠오르지 않아서 다른 사람 코드를 확인했음
다들 로직은 비슷한데 pop을 사용해서 시간복잡도를 낮추는 방향을 잡는듯
그래서 살짝 눈팅만하고 직접 구현하였음.
'''
def solution(numbers):
    answer = [-1]*len(numbers)
    stack = []
    for i in range(0,len(numbers)):
        while stack:
            if numbers[i] > numbers[stack[-1]]:
                answer[stack.pop()] = numbers[i]
            else: 
                stack.append(i)
                break
        else: stack.append(i)
                
    return answer
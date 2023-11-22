def solution(A, B):
    # 10만개 데이터이니 sort 사용하여 nlogn 시간복잡도도 괜찮을 것이라 판단
    # A,B를 모두 정렬하여 greedy 형식으로 풀려 시도 
    # 테스트케이스 17번만 계속 틀려서 고민중
    A.sort(reverse = True)
    B.sort(reverse = True)
    answer = 0
    pointer = 0
    for a in A:
        if a < B[pointer]:
            answer += 1
            pointer += 1
        
    return answer
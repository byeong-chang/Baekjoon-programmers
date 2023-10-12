def solution(n, s):
    '''
    일단 기본적으로 분할된 값들이 근처 값들일 경우에 곱했을 때 가장 크지 않을까?
    그럼 s의 몫과 나머지를 구해서 연속된 값들을 찾아서 리턴 넘기면 되지 않을까?
    일단 만들어 리스트로 만들고 sum과 min 값 체크해서 값 세부조정을 해준다.
    레츠기릿
    '''
    answer = [s//n for i in range(n)]
    if s%n:
        for i in range(s%n): answer[i] += 1
    if answer[-1] <1:
        return [-1]
    answer.reverse()
    return answer
def solution(A, B):
    for i in range(len(A)):
        if B == A[len(A)-i:]+ A[0:len(A)-i] :
            return i
    return -1
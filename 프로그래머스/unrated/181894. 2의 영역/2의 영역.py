def solution(arr):
    answer = [i for i,val in enumerate(arr) if val == 2]
    if answer:
        return arr[answer[0] : answer[-1]+1]
    else: return [-1]
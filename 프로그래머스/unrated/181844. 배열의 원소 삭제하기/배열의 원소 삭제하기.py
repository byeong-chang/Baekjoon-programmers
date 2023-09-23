def solution(arr, delete_list):
    answer = [i for i in arr if i not in delete_list]
    return answer
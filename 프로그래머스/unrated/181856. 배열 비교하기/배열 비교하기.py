def solution(arr1, arr2):
    leng1 , leng2 = len(arr1), len(arr2)
    if leng1 == leng2 :
        if int(sum(arr1) > sum(arr2)):
            return 1
        elif int(sum(arr1) < sum(arr2)):
            return -1
        else: return 0
    elif leng1 > leng2:
        return 1
    else: return -1
        
    answer = 0
    return answer
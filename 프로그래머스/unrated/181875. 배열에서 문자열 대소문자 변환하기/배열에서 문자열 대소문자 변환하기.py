def solution(strArr):
    strArr = [strArr[val].lower() if val%2 == 0 else strArr[val].upper() for val in range(len(strArr))   ]
    return strArr
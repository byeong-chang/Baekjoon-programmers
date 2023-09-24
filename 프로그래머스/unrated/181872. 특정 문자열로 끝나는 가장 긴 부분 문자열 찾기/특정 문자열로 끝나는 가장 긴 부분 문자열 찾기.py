def solution(myString, pat):
    length = len(pat)
    if pat == myString[-length:]:
        return myString
    for i in range(1,len(myString)-length+1):
        if pat == myString[-(i+length):-i]:
            return myString[:-i]
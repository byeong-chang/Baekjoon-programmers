def solution(arr):
    stk,i,length = [],0,len(arr)
    while i < length:
        if not stk:
            stk.append(arr[i])
            i+=1
        else:
            if stk[-1] == arr[i]:
                stk.pop()
                i+=1
            else:
                stk.append(arr[i])
                i+=1
    if stk:
        return stk
    else: return [-1]
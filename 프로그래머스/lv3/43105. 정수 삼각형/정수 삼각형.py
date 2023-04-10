def solution(triangle):
    lst = []
    
    for layer in triangle:
        if len(layer)== 1 : 
            lst.append(layer)
            continue
        max_len = len(layer)
        temp = []
        for i in range(max_len):
            if i == 0:
                temp.append(lst[-1][i] + layer[i])
            elif i == max_len-1:
                temp.append(lst[-1][i-1] + layer[i])
            else: temp.append(max(lst[-1][i] ,lst[-1][i-1]) +layer[i])    
        lst.append(temp)   
    return max(lst[-1])

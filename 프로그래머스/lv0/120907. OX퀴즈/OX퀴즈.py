def solution(quiz):
    answer = []
    for val in quiz:
        op, result = val.split('=')
        op = op.split()
        if op[1] =='+': 
            comp = int(op[0]) + int(op[2])
        else:  
            comp = int(op[0]) - int(op[2])
        if comp == int(result): answer.append('O')
        else: answer.append('X')
    return answer
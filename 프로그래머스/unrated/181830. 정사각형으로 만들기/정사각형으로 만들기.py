def solution(arr):
    row, column = len(arr),len(arr[0])
    if row > column:
        temp = [0 for _ in range(row - column)]
        for i in range(len(arr)):
            arr[i].extend(temp)
    elif row < column:
        temp = [0 for _ in range(column)]
        for i in range(column - row):
            arr.append(temp)
    return arr
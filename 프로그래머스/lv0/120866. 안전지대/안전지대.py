def solution(board):
    lenx ,leny = len(board[0]),len(board)
    temp = [[0]*lenx for _ in range(leny)]
    answer = 0
    for i in range(leny):
        for j in range(lenx):
            
            if board[i][j] == 1 :
                for x in range(-1,2):
                    for y in range(-1,2):
                        dy = i + y
                        dx = j + x
                        if dy >-1 and dy < leny and dx> -1 and dx < lenx:
                            temp[dx][dy] = -1
    return lenx * leny + sum(sum(i) for i in temp)
def solution(board, h, w):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    answer = 0
    color = board[h][w]
    for i in range(4):
        tx,ty = h + dx[i] , w + dy[i]
        if tx < len(board) and ty < len(board) and tx > -1 and ty > -1 and color == board[tx][ty]:
            answer+=1
        
    return answer
def solution(m, n, board):
    answer = 0
    while True:
        # 검사하기
        erased = []
        for i in range(m-1):
            for j in range(n-1):
                temp = board[i][j]
                if temp == ' ':  continue
                if temp == board[i+1][j+1] and temp == board[i+1][j] and temp == board[i][j+1]:
                    erased.append([i,j])
        # 검사 결과 변화가 없다면 반환하기
        if len(erased) == 0 :
            for k in range(m):
                answer += board[k].count(' ')
            return answer
        # 검사 반영하기
        for y,x in erased:
            board[y] = board[y][:x] + ' '*2 + board[y][x+2:]
            if x+2 == n:
                board[y+1] = board[y+1][:x] + ' '*2
            else:
                board[y+1] = board[y+1][:x] + ' '*2 + board[y+1][x+2:]
        # 당겨서 정리하기
        pulled = []
        for i in range(n):
            temp = ''
            for j in range(m):
                if board[j][i] != " ":
                    temp += board[j][i]
            
            temp = ' '*(m-len(temp)) + temp
            pulled.append(temp)
        for i in range(m):
            temp = ''
            for j in range(n):
                temp += pulled[j][i]
            board[i] = temp
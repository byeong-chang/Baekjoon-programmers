def solution(n, computers):
    answer = 0
    for k in range(len(computers)):
        stack = [k]
        if sum(computers[k]) != 0:
            while stack:
                start = stack.pop(0)
                computers[start][start] = 0
                for i in range(len(computers)):
                    if computers[start][i] == 1:
                        stack.append(i)
                        computers[start][i] = 0
                        computers[i][start] = 0
            answer+=1
    return answer

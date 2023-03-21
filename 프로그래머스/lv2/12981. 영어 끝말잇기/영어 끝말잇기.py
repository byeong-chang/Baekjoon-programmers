def solution(n, words):
    temp = [words[0]]
    for i in range(1,len(words)):
        if words[i-1][-1] != words[i][0]:
            return [i%n+1, i//n+1]
        elif words[i] in temp:
            return [i%n+1, i//n+1]
        temp.append(words[i])
    return [0,0]
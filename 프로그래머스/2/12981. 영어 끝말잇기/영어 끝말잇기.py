'''
스택에 계속 쌓아가면서
끝말잇기 체크
같은 단어 있는지 체크
for문 정상 종료시 [0,0]반환
'''
def solution(n, words):
    temp = [words[0]]
    for i in range(1,len(words)):
        if words[i-1][-1] != words[i][0]:
            return [i%n+1, i//n+1]
        elif words[i] in temp:
            return [i%n+1, i//n+1]
        temp.append(words[i])
    return [0,0]
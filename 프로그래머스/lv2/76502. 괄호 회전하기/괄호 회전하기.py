# 1. s에 저장된 문자를 다 돌려봐야하므로 n번 반복
# 2. 올바른 괄호 문자열 판별 알고리즘 <- Stack구현
# Stack 구현을 다 조건식으로 하는게 맞을까? c었으면 문자별 아스키 코드로 처리했을거 같은데
# 
def solution(s):
    answer = 0
    for i in range(len(s)):
        stack = []
        flag = True
        for j in (s[i:] + s[:i]):
            if j == "[" or j == "(" or j == "{":
                stack.append(j)
            else:
                if len(stack) == 0:
                    flag = False
                    break
                temp = stack.pop()
                if j == "]" and temp == "[" or j == ")" and temp == "(" or j == "}" and temp =="{":
                    continue
                else:
                    flag = False
                    break
        if flag and not stack: answer +=1
    return answer
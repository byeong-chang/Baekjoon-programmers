def solution(begin, target, words):
    '''
    한 10분 고민해봤는데 좋은 로직이 떠오르지 않는다. 아래방식으로 구현해보고 안되면 답지를 보자
    바꿀 수 있으면 무조건 바꾸는 로직(내가 3글자고 2글자 같은애를 발견하면 일단 걔로 변경)
    근데 이렇게 해버리면 시간 복잡도가 지수 급인데..
    '''
    if target not in words: return 0
    stack = [[begin,0]]
    length,n = len(begin),len(words)
    while stack:
        word,time = stack.pop()
        if time > n: continue
        for w in words:
            count = 0
            for i in range(length):
                if word[i] == w[i] : count+=1
            if count == length-1:
                if w == target:
                    print(w,target,time)
                    return time+1
                stack.append([w,time+1])
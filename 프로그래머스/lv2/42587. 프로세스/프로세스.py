def solution(priorities, location):
    answer = 0
    # 0 위치에 있는 놈 반복적으로 pop 할 예정.
    # return 할 때 마다 answer 값 1 씩 늘려준다.
    # location인 놈이 return 될 때 반복 종료를 어떻게 시키느냐?
    # 1. location 값을 반복문 돌 때 마다 옮겨준다. (ex 2->1->0) location = 0 일 때 return 되면 그 때 종료시키기. 말고는 안 떠오르네 이걸로 진행시켜
    while True:
        flag = True
        priority = priorities.pop(0)
        location -=1
        
        for val in priorities:
            if val > priority:
                priorities.append(priority)
                if location == -1 :
                    location = len(priorities) -1
                flag = False
                break
        if flag:
            answer +=1
            print(priorities)
            if location == -1 :
                return answer
        
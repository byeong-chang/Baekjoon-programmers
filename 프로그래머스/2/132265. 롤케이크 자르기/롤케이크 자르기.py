from collections import Counter
def solution(topping):
    answer = 0
    counter = Counter(topping)
    front = set()
    back = len(counter)
    for top in topping:
        front.add(top)
        temp = len(front)
        counter[top]-=1
        if counter[top] == 0 :
            back-=1
        if temp == back:
            answer+=1
        elif temp > back:
            return answer
    return answer
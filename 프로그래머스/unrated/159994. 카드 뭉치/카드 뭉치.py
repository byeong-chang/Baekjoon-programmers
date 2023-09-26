def solution(cards1, cards2, goal):
    if len(goal) > len(cards1) + len(cards2):
        return "No"
    while goal:
        if cards1 and goal[0] == cards1[0]:
            cards1.pop(0)
            goal.pop(0)
        elif cards2 and goal[0] == cards2[0]:
            cards2.pop(0)
            goal.pop(0)
        else: return "No"
    return "Yes"
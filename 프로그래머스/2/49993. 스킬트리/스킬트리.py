def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        pointer = 0
        for s in skill_tree:
            if s in skill:
                if skill[pointer] == s:
                    pointer+=1
                else: break
        else:
            answer+=1
    return answer
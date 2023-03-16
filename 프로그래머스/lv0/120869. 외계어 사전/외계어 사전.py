def solution(spell, dic):
    for text in dic:
        Flag = True
        temp = spell.copy()
        
        if len(text) != len(spell): 
            continue
        
        for i in text:
            if i in temp:
                temp.remove(i)
            else:
                Flag = False
                break
        if Flag:
            return 1
    return 2
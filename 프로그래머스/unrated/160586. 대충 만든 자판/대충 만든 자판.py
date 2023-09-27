def solution(keymap, targets):
    keymapword = []
    for key in keymap:
        keymapword.extend([i for i in key])
    keymapword = list(set(keymapword))
    dic = dict()
    for i in keymapword:
        temp = []
        for key in keymap:
            x = key.find(i)
            if x != -1:
                temp.append(x)
        dic[i] = min(temp)+1
    answer = []
    for target in targets:
        temp = []
        for w in target:
            if w not in dic:
                answer.append(-1)
                break
            else: temp.append(dic[w])
        else: answer.append(sum(temp))
    return answer
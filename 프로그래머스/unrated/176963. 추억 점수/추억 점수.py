def solution(name, yearning, photo):
    answer= []
    dic = {name[i] : yearning[i] for i in range(len(name))}
    for i in photo:
        total = 0
        for j in i:
            if j in dic:
                total += dic[j]
        answer.append(total)
    return answer
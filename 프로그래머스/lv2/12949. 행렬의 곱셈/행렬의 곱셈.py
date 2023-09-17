def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp = [[] for i in range(len(arr2[0]))]
        answer.append(temp)
    for i in range(len(arr1)):
        for k in range(len(arr2[0])):
            for j in range(len(arr1[0])):
                    answer[i][k].append(arr1[i][j]* arr2[j][k])
            answer[i][k] = sum(answer[i][k])
    print(answer)
    return answer
def solution(n, arr1, arr2):
    arr1_str = []
    arr2_str = []
    for i in arr1:
        string = []
        for j in range(n):
            string.append(i%2)
            i//=2
        string.reverse()
        arr1_str.append(string)
    for i in arr2:
        string = []
        for j in range(n):
            string.append(i%2)
            i//=2
        string.reverse()
        arr2_str.append(string)
    answer = []
    for i in range(n):
        lst = ''
        for j in range(n):
            if arr1_str[i][j] == 1 or arr2_str[i][j] == 1 :
                lst+= '#'
            else: lst+=' '
        answer.append(lst)
    return answer
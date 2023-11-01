def solution(files):
    nums = ['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(files)):
        head,number,tail = '','',''
        for j in range(len(files[i])):
            if files[i][j] in nums:
                head = files[i][:j]
                number = files[i][j:]
                break
        for k in range(1,len(number)):
            if number[k] not in nums:
                tail = number[k:]
                number = number[:k]
                break
        files[i] = [head,number,tail]
    files.sort(key = lambda x : (x[0].lower(),int(x[1])) )
    
    for i in range(len(files)):
        files[i] = ''.join(files[i])
    return files
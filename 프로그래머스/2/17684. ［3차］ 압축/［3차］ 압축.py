def solution(msg):
    answer,count = [],27
    mapping = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
    'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
    'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}
    
    # 문자를 늘려가며 mapping에 없다면 이전 값을 answer에 넣어주고, 새 값을 mapping에 추가해주는 것을 반복 
    i,length = 0,len(msg) 
    while True:
        j = 2
        while i+j <= length:
            if msg[i:i+j] not in mapping:
                mapping[msg[i:i+j]] = count
                count+=1
                answer.append(mapping[msg[i:i+j-1]])
                i += (j-1)
                break
            j+=1
        else:
            answer.append(mapping[msg[i:]])
            break
        
    return answer
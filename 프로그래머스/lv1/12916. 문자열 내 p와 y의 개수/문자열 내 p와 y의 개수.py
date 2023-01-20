def solution(s):
    answer = True
    count =0
    for i in s:
        if i == 'p' or i == 'P':
            count+=1
        elif i == 'Y' or i == 'y':
            count-=1
    if count !=0:
        answer = False
        
    return answer
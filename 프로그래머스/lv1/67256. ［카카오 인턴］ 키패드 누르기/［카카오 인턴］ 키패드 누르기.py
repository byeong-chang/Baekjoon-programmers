def solution(numbers, hand):
    answer = ''
    left = [0,3]
    right = [2,3]
    two_to_zero = {2:0,5:1,8:2,0:3}
    
    for number in numbers:
        if number in [1,4,7]: 
            answer+= 'L'
            left = [0,[1,4,7].index(number)]
        elif number in [3,6,9] :
            answer+='R'
            right = [2,[3,6,9].index(number)]
        else:
            current = [1,two_to_zero[number]]
            ldiff = abs(left[0] - current[0]) + abs(left[1] - current[1])
            rdiff = abs(right[0] - current[0]) + abs(right[1]- current[1])
            if ldiff > rdiff:
                right = current.copy()
                answer+='R'
            elif ldiff < rdiff:
                left = current.copy()
                answer+='L'
            else: 
                if hand == 'right': 
                    answer+='R'
                    right = current.copy()
                else : 
                    answer+='L'
                    left = current.copy()
                        
    return answer
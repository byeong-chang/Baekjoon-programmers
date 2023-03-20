def solution(sizes):
    big_x = 0
    big_y = 0
    sizes = [[size[0],size[1]]  if size[0]> size[1] else [size[1],size[0]] for size in sizes]
    for size in sizes:
        if size[0] > big_x : big_x = size[0]
        if size[1] > big_y : big_y = size[1]
        
    answer = big_x *big_y 
    return answer
def GCD(x,y):
    while(y):
        x,y = y,x%y
    return x

def LCM(x,y):
    return (x*y) // GCD(x,y)
    
def solution(arr):
    answer = 0
    while len(arr)>1:
        v1 = arr.pop()
        v2 = arr.pop()
        arr.append(LCM(v1,v2))
        
    return arr[0]
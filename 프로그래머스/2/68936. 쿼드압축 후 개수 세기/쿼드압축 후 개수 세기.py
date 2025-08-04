answer = [0,0]
def solution(arr):
    
    compress(arr,len(arr),0,0)
    
    return answer

def compress(arr,n,x,y):
    if n == 1:
        answer[arr[x][y]] +=1
        return
    
    origin = arr[x][y]
    flag = True
    for i in range(n):
        for j in range(n):
            if origin != arr[x+i][y+j]:
                flag = False
                break
    if flag:
        answer[origin] +=1
    else:
        compress(arr,n//2,x,y)
        compress(arr,n//2,x+n//2,y)
        compress(arr,n//2,x,y+n//2)
        compress(arr,n//2,x+n//2,y+n//2)
                
    
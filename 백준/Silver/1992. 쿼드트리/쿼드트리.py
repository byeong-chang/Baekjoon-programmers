import sys
N = int(sys.stdin.readline())
video = [sys.stdin.readline().strip() for i in range(N)]
compression = ""
def four_divide(x,y,num):
    global compression
    if num <= 1:
        compression +=video[x][y]
        return
    first_value = video[x][y]
    flag = True
    for i in range(num):
        for j in range(num):
            if first_value !=video[x+i][y+j]:
                flag = False
                compression += "("
                four_divide(x,y,num//2)
                four_divide(x,y+num//2,num//2)
                four_divide(x+num//2,y,num//2)
                four_divide(x+num//2,y+num//2,num//2)
                compression +=")"
                return
    if flag == True: compression += first_value

four_divide(0,0,N)
print(compression)
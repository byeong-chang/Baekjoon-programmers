import sys
N = int(sys.stdin.readline())
input_list = [list(map(int,sys.stdin.readline().split())) for i in range(N)]
count=[0,0,0]

def recursive_search(x,y,n):
    temp = input_list[x][y]
    global count
    for i in range(x,x+n):
        for j in range(y,y+n):
            if input_list[i][j] == temp:
                continue
            else :
                for k in range(x,x+n,n//3):
                    for l in range(y,y+n,n//3):
                        recursive_search(k,l,n//3)
                return 0
    count[temp+1] +=1

recursive_search(0,0,N)
print("{}\n{}\n{}".format(count[0],count[1],count[2]))
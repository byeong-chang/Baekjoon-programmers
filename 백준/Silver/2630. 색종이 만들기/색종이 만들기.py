import sys
N = int(sys.stdin.readline())
paper_lst = [list(map(int,sys.stdin.readline().split())) for i in range(N)]
blue_count = 0
white_count = 0
def color_check(x,y,length):
    global blue_count,white_count
    if length == 1:
        if paper_lst[x][y] == 0:
            white_count +=1
        else: blue_count +=1
        return
    check = paper_lst[x][y]
    for i in range(length):
        for j in range(length):
            if paper_lst[x+i][y+j] != check:
                color_check(x,y,length//2)
                color_check(x+length//2,y,length//2)
                color_check(x,y+length//2,length//2)
                color_check(x+length//2,y+length//2,length//2)
                return
    if check == 0:
        white_count +=1
    else: blue_count +=1

color_check(0,0,N)
print(white_count,blue_count,sep="\n")
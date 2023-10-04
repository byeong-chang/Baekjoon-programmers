def solution(wallpaper):
    temp = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                temp.append([i,j])
    temp.sort(key = lambda x: x[1])
    y = [ temp[0], temp[-1]] 
    temp.sort()
    x = [temp[0],temp[-1]]
    answer = [x[0][0],y[0][1],x[1][0]+1,y[1][1]+1]
    return answer
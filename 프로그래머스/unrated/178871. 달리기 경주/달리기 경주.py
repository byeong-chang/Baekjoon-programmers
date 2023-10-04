def solution(players, callings):   
    dic = {player : i for i,player in enumerate(players)}
    for call in callings:
        i = dic[call]
        dic[players[i-1]] +=1
        dic[call] -=1
        players[i],players[i-1] = players[i-1],players[i]
        
    return players
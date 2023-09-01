def solution(genres, plays):
    # 노래 개수만큼 반복 돌려서 딕셔너리로 장르 별 [id , play회수]를 담은 후 정렬 필요
    # 정렬 기준은 play횟수, -id 순서
    # 딕셔너리 기준으로 반복문을 돌려서 가장 큰 2개씩 리턴 때림
    bestAlbum = dict()
    answer = []
    #dict 만들기
    for i in range(len(genres)):
        if genres[i] in bestAlbum:
            bestAlbum[genres[i]][0][0] += plays[i]
            bestAlbum[genres[i]].append([plays[i],i])
        else: 
            bestAlbum[genres[i]] = [[plays[i],-1],[plays[i],i]]
            
    # 앨범 장르 개수 높은 순 정렬
    bestAlbum = sorted(bestAlbum.items(), key = lambda item : item[1][0][0],reverse = True)
    # 장르별 정렬 및 answer에 추가
    for key, values in bestAlbum:
        values = sorted(values, key = lambda x : (-x[0], x[1]))
        answer.append(values[1][1])
        if len(values) >2: 
            answer.append(values[2][1])
    return answer
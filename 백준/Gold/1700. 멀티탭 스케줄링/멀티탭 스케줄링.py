N,K = map(int,input().split())
lst = list(map(int,input().split()))
count = 0
tap = set()
# 멀티탭이 다 찼을때 어느 전기용품을 뽑을지 정하는 함수
def order(tap,index):
    global count
    max = 0
    min_index = 0
    temp = lst[index:] # 남은 검사할 값들을 slicing으로 저장함.
    for i in tap:
        try: 
            tmp = temp.index(i) # valueError발생 가능
            if tmp >= max: # 최대한 늦게 불리는 놈을 찾는다.
                max = tmp
                min_index = i
        except:# 다시 불리지 않는 전자기기는 예외처리가 발생하며 즉시 이 값을 빼주면 된다.
            tap.remove(i)
            tap.add(lst[index])
            count+=1
            return
    tap.remove(min_index) # 예외가 발생하지 않으면 다시 불리지 않는 전자기기는 없다는 뜻
    tap.add(lst[index]) # 가장 멀리서 다시 불리는 기기를 삭제하고 현재 값 넣어준 후 카운트 증가
    count+=1

for i in range(K):
    if lst[i] in tap: # 중복값이 들어오면 pass
        continue
    if len(tap) >= N: # 멀티탭이 가득 차면
        order(tap,i) # 함수실행
    else: # 멀티탭이 가득 안찼고, 중복값도 아니면 
        tap.add(lst[i])# 값 추가.
print(count)
import sys
lst = []
sum_lst=[]

n = int(sys.stdin.readline())
for _ in range(n):
    lst.append(int(sys.stdin.readline()))
if n==2:
    print(lst[0]+lst[1])
    exit()
if n==1:
    print(lst[0])
    exit()
#case 1 n-2 까지 도달하는 가장 최선의 값 + n번째 값  
#case 2 n-1 까지 도달하는 가장 최선의 값 + n번째 값 + n-3까지 도달하는 가장 최선의 값(3번 연속된 발판을 밟을 수는 없기 때문에)
sum_lst.append(lst[0])
sum_lst.append(max(sum_lst[0]+lst[1],lst[1]))
sum_lst.append(max(sum_lst[0]+lst[2],lst[1]+lst[2]))
for i in range(3,n):
    sum_lst.append(max(sum_lst[i-2]+lst[i],lst[i-1]+lst[i]+sum_lst[i-3]))
print(sum_lst[-1])
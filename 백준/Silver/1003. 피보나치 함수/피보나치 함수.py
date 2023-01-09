import sys
T = int(sys.stdin.readline())
fib_lst = [[1,0],[0,1]]
input_lst = []
for i in range(T):
    input_lst.append(int(sys.stdin.readline()))

for i in range(2,max(input_lst)+1):
    fib_lst.append([fib_lst[i-2][0]+fib_lst[i-1][0], fib_lst[i-2][1]+fib_lst[i-1][1]])

for i in range(T):
    print("{} {}".format(fib_lst[input_lst[i]][0],fib_lst[input_lst[i]][1]))

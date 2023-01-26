for i in range(int(input())):
    M,N,x,y = map(int,input().split())
    Flag = False
    if M>=N:
        for i in range(x,M*N+1,M):
            if i%N == y%N:
                Flag = i
                break
    else:
        for i in range(y,M*N+1,N):
            if i%M == x%M:
                Flag = i
                break
    if Flag != False:
        print(Flag)
    else: print(-1)
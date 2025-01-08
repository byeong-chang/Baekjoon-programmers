import sys
n = int(sys.stdin.readline())
stack = [int(sys.stdin.readline()) for i in range(n)]
sorted_stack = sorted(stack)
solve =[]
answer = ""
while stack :
    if sorted_stack:
        solve.append(sorted_stack.pop(0))
        answer+="+"
    while solve and stack:
        if solve[-1]==stack[0]:
            answer+="-"
            stack.pop(0)
            solve.pop(-1)
        elif solve[-1]!=stack[0] and  not sorted_stack:
            print("NO")
            answer = ""
            stack = []
            break
        else : break
for i in answer:
    print(i)
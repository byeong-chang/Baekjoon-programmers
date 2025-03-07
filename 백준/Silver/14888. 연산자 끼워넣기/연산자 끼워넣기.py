import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
m = n-1
nums = list(map(int,input().split()))
operators = list(map(int,input().split()))
lst = ["+", "-" , "*", "/"]
sel = [0 for _ in range(m)]
answer = [-float("inf"),float("inf")]

def perm(depth):

    if depth == m:
        operate()
        return

    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            sel[depth] = lst[i]
            perm(depth+1)
            operators[i] += 1

def operate():
    global answer
    total = nums[0]

    for i,op in enumerate(sel):
        if op == "+":
            total += nums[i+1]
        elif op == "-":
            total -= nums[i+1]
        elif op == "*":
            total *= nums[i+1]
        elif op == "/":
            if total <0:
                total = -(abs(total) // nums[i+1])
            else:
                total = total // nums[i+1]


    answer = [max(answer[0],total), min(answer[1],total)]

perm(0)
print(answer[0])
print(answer[1])
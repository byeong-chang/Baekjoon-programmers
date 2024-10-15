
import sys

def input():
    return sys.stdin.readline().rstrip()
    

lst = ['qwertyuiop' ,'asdfghjkl' , 'zxcvbnm']
bowel = ['y','u','i','o','p','h','j','k','l','b','n','m']
left, right = input().split()
word = input()

def find(w):
    for i,key in enumerate(lst):
        temp = key.find(w)
        if temp != -1:
            return i,temp

left,right = find(left), find(right)

counting = 0
for w in word:
    y,x = find(w)
    if w in bowel:
        hand = abs(right[0] - y) + abs(right[1] - x)
        right = y,x
    else:
        hand =  abs(left[0] - y) + abs(left[1] - x)
        left = y,x

    counting += hand+1
print(counting)
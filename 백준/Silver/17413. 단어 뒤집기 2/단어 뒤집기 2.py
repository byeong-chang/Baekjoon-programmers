'''단순 구현 문제
<를 만난 경우에는 공백을 무시하고 > 만날때까지 기다려야함
공백을 만난 경우에는 뒤집어서 출력해야함.
'''
import sys

def input():
    return sys.stdin.readline().rstrip()


s = input()

temp,flag,words ='',True,[]
for w in s:

    if w == '<':
        flag = False
        words.append(temp)
        temp = ""
    
    if w == ">":
        flag = True
        temp +=">"
        words.append(temp)
        temp = ""
        continue

    if w == " "and flag:
        words.append(temp)
        words.append(" ")
        temp = ""
        continue

    temp += w

words.append(temp)
for word in words:
    if word == "":
        pass
    elif word[0] == '<':print(word,end = '')
    else: print(word[::-1],end = '')
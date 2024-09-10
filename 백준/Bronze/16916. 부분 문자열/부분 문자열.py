import sys

text = sys.stdin.readline().rstrip()
answer = sys.stdin.readline().rstrip()
if answer in text: print(1)
else: print(0)
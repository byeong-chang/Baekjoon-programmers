import sys

result = ""
while True:
    text = sys.stdin.readline().rstrip()
    if text == "END":
        print(result[:-1])
        break
    
    result += text[::-1] + "\n"
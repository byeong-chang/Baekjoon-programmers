import sys

words = [sys.stdin.readline().rstrip() for _ in range(5)]
max_length = max([len(word) for word in words])
result = ""

for word in range(len(words)):
    words[word] += " " * (max_length - len(words[word]))

for i in range(max_length):
    for j in range(5):
        result += words[j][i]

print(result.replace(" ", ""))
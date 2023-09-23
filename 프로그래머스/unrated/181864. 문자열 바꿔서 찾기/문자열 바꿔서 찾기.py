def solution(myString, pat):
    myString = ''.join(['B' if i == "A" else 'A' for i in myString])
    return int(pat in myString)
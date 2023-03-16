def solution(s):
    count_zero = 0
    count_bi = 0
    while s != "1":
        count_zero += s.count("0")
        s = s.replace("0","")
        s = bin(len(s))[2:]
        count_bi +=1
    return [count_bi,count_zero]



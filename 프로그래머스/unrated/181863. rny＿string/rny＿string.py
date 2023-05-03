def solution(rny_string):
    answer = ['rn' if i == "m" else i  for i in rny_string ]
    return "".join(answer)
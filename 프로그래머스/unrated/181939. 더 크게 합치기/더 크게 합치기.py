def solution(a, b):
    type1 = int(str(a)+str(b))
    type2 = int(str(b)+str(a))
    if type1 > type2:
        return type1
    else: return type2
def solution(order):
    answer = 0
    for o in order:
        if 'americano' in o or 'anything' in o:
            answer+=4500
        else: answer+=5000
    return answer
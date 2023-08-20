import math 
def solution(fees, records):
    stacks = dict()
    def calTime(IN,OUT):
        time = 0
        h1,m1 = map(int,IN[0].split(":"))
        h2,m2 = map(int,OUT.split(":"))
        return ((h2-h1)*60 + (m2-m1))
    def calFee(time):
        if time >fees[0]:
            return fees[1] + math.ceil((time-fees[0])/fees[2])*fees[3]
        else: return fees[1]
    for record in records:
        record = record.split()
        if record[2] == "IN":
            if int(record[1]) in stacks:
                stacks[int(record[1])][0] = record[0]
                stacks[int(record[1])][2] = 1
            else: 
                stacks[int(record[1])] = [record[0],0,1]
        else:
            stacks[int(record[1])][1] += calTime(stacks[int(record[1])],record[0])
            stacks[int(record[1])][2] = 0
    for stack in stacks.values():
        if stack[2] == 1:
            stack[1] += calTime(stack,'23:59')
    print()
    answer = [calFee(val[1][1]) for val in sorted(stacks.items())]
    return answer